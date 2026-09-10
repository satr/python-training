# Dictionaries and sets

## Theory

Dictionaries associate unique keys with values and are well suited to counts.
Sets store unique members and support operations such as intersection. Sorting
a set-derived result makes its order deterministic.

## Learn before coding

Use `counts[word] = counts.get(word, 0) + 1` to update a dictionary counter;
`.get` supplies a value when a key is absent. Sets remove duplicates, and
`left & right` is their intersection. For example, counting `["red", "blue",
"red"]` gives `{"red": 2, "blue": 1}`, while `{"a", "b"} & {"b", "c"}`
contains only `"b"`. Build counters in input order when predictable output
matters, sort a set-derived result before returning it, and do not mutate
caller-owned sets or assume set iteration order is stable.

## Task

Implement `count_items` to count each string and `common_items` to return the
sorted strings present in both input sets.

## Run

```bash
make 01_core_06_dictionaries_and_sets
```

## Further practice

Build a frequency table ordered by count and find items unique to either set.
