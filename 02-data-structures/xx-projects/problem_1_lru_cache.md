# Least Recently Used Cache

## Runtime complexity

The runtime complexity of this solution is *linear*, _O(n)_ based on these collective complexities:

`get` (HashSet): _O(1)_ int he average case, _O(n)_ in the worst case
`set` (HashSet): *Constant* _O(1)_

deletion at the head when adding a new element (dictionary): *Constant* _O(1)_

search for deleting and adding to tail (dictionary): _O(n)_

## Memory complexity

The memory complexity of this solution is *linear*, _O(n)_ where _n_ is the size of the cache.
## References

- [JournalDev: Python OrderedDict](https://www.journaldev.com/21807/python-ordereddict)
- [algo-en: LRU Cache Strategy in Detial](https://labuladong.gitbook.io/algo-en/ii.-data-structure/lru_algorithm)
