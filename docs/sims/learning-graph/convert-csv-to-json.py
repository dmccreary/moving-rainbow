#!/usr/bin/env python3
"""
Convert moving-rainbow.csv to moving-rainbow.json
CSV format: ConceptID,ConceptName,DependsOn,TaxonomyID
JSON format: {nodes: [{id, label, group}], edges: [{from, to}]}
"""

import csv
import json

def convert_csv_to_json(csv_file, json_file):
    nodes = []
    edges = []

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            concept_id = int(row['ConceptID'])
            concept_name = row['ConceptName']
            depends_on = row['DependsOn'].strip()
            taxonomy_id = row['TaxonomyID']

            # Create node
            nodes.append({
                'id': concept_id,
                'label': concept_name,
                'group': taxonomy_id
            })

            # Create edges from dependencies
            if depends_on:
                # Split by pipe for multiple dependencies
                dependencies = [d.strip() for d in depends_on.split('|') if d.strip()]
                for dep in dependencies:
                    try:
                        dep_id = int(dep)
                        edges.append({
                            'from': dep_id,
                            'to': concept_id
                        })
                    except ValueError:
                        print(f"Warning: Invalid dependency '{dep}' for concept {concept_id}")

    # Create the final JSON structure
    graph_data = {
        'nodes': nodes,
        'edges': edges
    }

    # Write to JSON file
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(graph_data, f, indent=4)

    print(f"Converted {len(nodes)} nodes and {len(edges)} edges")
    print(f"Output written to {json_file}")

if __name__ == '__main__':
    convert_csv_to_json('moving-rainbow.csv', 'moving-rainbow.json')
