# Concept Depend

!!! prompt
    Please create a fully connected concept dependency graph for the concepts in this course.
    Start with the concepts in /docs/concept-sequence.md
    For each Concept on this list below, create a new
    list of other concepts on which it depends.  If a concept
    depends on a specific concept that is not listed,
    then we will need to add it as a new concept.
    This will help us determine the teaching order of the Concepts.

Return the new list as a CSV file using the following format:

1. The first column in the CSV file is a numeric concept
ID you assigned in the list above.
2. The second column is the concept name.
3. The third column is a pipe-delimited list of the Concept IDs that the concept depends upon.

Check your results to make sure that all concepts are connected to at least one other concept.

Place the results in /data/learning-graph.csv
