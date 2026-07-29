#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

let Ajv2020;
let addFormats;

try {
  Ajv2020 = require("ajv/dist/2020");
  addFormats = require("ajv-formats");
} catch (error) {
  console.error("De Node-pakketten 'ajv' en 'ajv-formats' zijn vereist voor deze controle.");
  console.error(error.message);
  process.exit(1);
}

const [, , schemaFile, releaseDir] = process.argv;

if (!schemaFile || !releaseDir) {
  console.error("Gebruik: validate_json_examples.js <schema.json> <release-directory>");
  process.exit(2);
}

if (!fs.existsSync(schemaFile)) {
  console.error(`JSON-schema bestaat niet: ${schemaFile}`);
  process.exit(1);
}

if (!fs.existsSync(releaseDir)) {
  console.error(`Release-directory bestaat niet: ${releaseDir}`);
  process.exit(1);
}

const exampleFiles = fs
  .readdirSync(releaseDir)
  .filter((file) => file.endsWith("Voorbeeld.json"))
  .sort()
  .map((file) => path.join(releaseDir, file));

if (exampleFiles.length === 0) {
  console.error(`Geen voorbeeldbestanden gevonden in ${releaseDir}`);
  process.exit(1);
}

const schema = JSON.parse(fs.readFileSync(schemaFile, "utf8"));
const ajv = new Ajv2020({ allErrors: true, strict: false });
addFormats(ajv);
const validate = ajv.compile(schema);

let hasErrors = false;

for (const exampleFile of exampleFiles) {
  const instance = JSON.parse(fs.readFileSync(exampleFile, "utf8"));

  if (!validate(instance)) {
    hasErrors = true;
    console.error(`ONGELDIG: ${exampleFile}`);
    for (const error of validate.errors ?? []) {
      console.error(`  ${error.instancePath || "/"} ${error.message}`);
    }
  } else {
    console.log(`Geldig: ${exampleFile}`);
  }
}

if (hasErrors) {
  process.exit(1);
}
