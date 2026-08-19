#!/usr/bin/env python3
"""Apply project-specific constraints to a Crunch UML JSON Schema."""

from __future__ import annotations

import html
import json
import sys
from pathlib import Path
from typing import Any


CLIENT_KEY = "client"
BSN_KEY = "burgerservicenummer"
CLIENT_DETAILS = [
    "postcode",
    "huisnummer",
]


def add_closed_objects(node: Any) -> None:
    """Close every object schema that does not explicitly define this setting."""

    if isinstance(node, dict):
        for value in node.values():
            add_closed_objects(value)

        if (
            (node.get("type") == "object" or "properties" in node)
            and node.get("additionalProperties") is not False
        ):
            node["additionalProperties"] = False
    elif isinstance(node, list):
        for value in node:
            add_closed_objects(value)


def decode_html_entities(node: Any) -> int:
    """Vervang HTML-entiteiten in omschrijvingen door het teken zelf.

    Enterprise Architect bewaart accenttekens in notities als entiteit (&#233;
    voor é). De Markdown-generator decodeert die, de JSON-schema-generator niet,
    waardoor ze letterlijk in de normatieve tekst belanden.
    """

    decoded = 0

    if isinstance(node, dict):
        for key in ("description", "title"):
            waarde = node.get(key)
            if isinstance(waarde, str):
                ontcijferd = html.unescape(waarde)
                if ontcijferd != waarde:
                    node[key] = ontcijferd
                    decoded += 1

        for value in node.values():
            decoded += decode_html_entities(value)
    elif isinstance(node, list):
        for value in node:
            decoded += decode_html_entities(value)

    return decoded


def sort_required_lists(node: Any) -> int:
    """Sorteer elke required-lijst alfabetisch.

    Crunch UML bouwt deze lijsten op uit een set, waardoor de volgorde per run
    verschilt. Dat levert diff-ruis op bij elke regeneratie van het schema.
    """

    sorted_lists = 0

    if isinstance(node, dict):
        required = node.get("required")
        if isinstance(required, list) and all(isinstance(name, str) for name in required):
            if required != sorted(required):
                node["required"] = sorted(required)
                sorted_lists += 1

        for value in node.values():
            sorted_lists += sort_required_lists(value)
    elif isinstance(node, list):
        for value in node:
            sorted_lists += sort_required_lists(value)

    return sorted_lists


def sort_defs(schema: Any) -> bool:
    """Zet de definities in $defs op alfabetische volgorde, om dezelfde reden."""

    if not isinstance(schema, dict):
        return False

    defs = schema.get("$defs")
    if not isinstance(defs, dict):
        return False

    volgorde = sorted(defs)
    if volgorde == list(defs):
        return False

    schema["$defs"] = {naam: defs[naam] for naam in volgorde}
    return True


def add_client_identity_constraint(node: Any) -> int:
    """Add the BSN-or-address identity rule to every client property found."""

    found = 0

    if isinstance(node, dict):
        properties = node.get("properties")
        if isinstance(properties, dict) and CLIENT_KEY in properties:
            client_schema = properties[CLIENT_KEY]
            if not isinstance(client_schema, dict):
                raise ValueError("De schema-definitie van client is geen object.")

            client_schema["oneOf"] = [
                {
                    "required": [BSN_KEY],
                    "properties": {BSN_KEY: {"minLength": 9, "maxLength": 9}},
                    "additionalProperties": False,
                },
                {
                    "not": {"required": [BSN_KEY]},
                    "required": CLIENT_DETAILS,
                },
            ]
            found += 1

        for value in node.values():
            found += add_client_identity_constraint(value)
    elif isinstance(node, list):
        for value in node:
            found += add_client_identity_constraint(value)

    return found


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Gebruik: {Path(sys.argv[0]).name} <schema.json>", file=sys.stderr)
        return 2

    schema_path = Path(sys.argv[1])
    if not schema_path.is_file():
        print(f"JSON-schema bestaat niet: {schema_path}", file=sys.stderr)
        return 1

    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        clients_updated = add_client_identity_constraint(schema)
        if clients_updated == 0:
            raise ValueError("Geen property 'client' gevonden in het JSON-schema.")
        add_closed_objects(schema)
        decoded = decode_html_entities(schema)
        sort_required_lists(schema)
        sort_defs(schema)
        schema_path.write_text(
            json.dumps(schema, indent=4, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"Postprocessing van JSON-schema mislukt: {error}", file=sys.stderr)
        return 1

    print(
        f"JSON-schema nagebewerkt: {clients_updated} client-definitie(s) "
        "voorzien van de identiteitsregel; objecten zijn gesloten; "
        f"{decoded} omschrijving(en) ontdaan van HTML-entiteiten; "
        "required-lijsten en $defs zijn alfabetisch gesorteerd."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
