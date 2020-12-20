Lec 24: Caches 1

Binary Prefixes
- Kilo, Mega, Giga, Tera, Peta, Exa, Zetta, Yotta: prefixes used for SI
	- Kilo = 2^ 10 = 1024 while SI is 1000 (bits go w/ powers of 10, not powers of 2 definition)
	- Cache, memory deal w/ base 2 representations (Ki = 1024)--need to distinguish b/w 
	  base 10 and base 2 reps to stay consistent
- Kibi = 2^10, Mebi = 2^20, Gibi = 2^30, Tebi = 2^40, Pebi = 2^50, Exbi = 2^60, Zebi = 2^70, Yebi = 2^80
	- Example calculations: 2^34 = 2^30 * 2^4 = 16 Gibi, 2^47 = 2^7 * 2^40 = 128 Tebi

Memory Hierarchy
- Slowness of memory: searching through many items takes a long time
	- Idea: want a large memory that does not require sacrifice in terms of speed
	- Want to be mimic the speed of a register but scale the size to that of a hard drive
- Disconnect b/w processor/memory speeds can be resolved w/ memory cache
	- Uses IC processing tech (same as CPU): fast but expensive compared to DRAM
	- Cache: copy of a subset of main memory. Most processors separate caches for instruction & data
-CPU/Registers: Registers that are on have direct access to the CPU are fast, expensive, and have small capacity
- DRAM/Physical Memory characteristics: fast, reasonably cheap, moderate capacity
- Caches exist in the layer in b/w CPU/Core & Physical Memory/RAM: in b/w characteristics of the 2
	- Idea: caches are much larger than registers, but only slightly slower
- Getting farther away from processor increases access time (slower). Larger distance increases not only
  physical distance but also the time it takes to take each step (2 barriers to speed)
  - Farther away from process? Increasing relative size of memory. Processor: words. Main Memory: 1-4 blocks (each
  	block is 8-32 bytes), Secondary Memory: 1024+ bytes. Per unit cost of larger memory also cheaper
- Memory is inclusive: lower layers of the memory hierarchy contains all the memory from the higher levels
- BIG IDEA: "illusion" of offering the memory of the cheap tech but the speed of the fast tech

Locality, Design, Measurement
- Cache: contains copies of data in memory (which contains copy of data on disk) that are used
	- Relies on temporal locality (stuff used now will be used again soon) and spacial locality (if certain
	  memory is used, likely will want to use neighboring components)
	- Temporal Locality: cache should remember memory (have a copy) that was recently used to be referenced
	- Spatial Locality: cache should grab blocks of contiguous memory closer to processor for ease of access
- Questions of cache design: organization, mapping memory address, num elements in cache, how to quickly locate
	- Need a way to choose b/w recently accessed copy generated by cache and when to grab directly from memory
	- Also need to know if the bits that a cache has are garbage bits or if they are valid representations
	- Since cache is subset of memory, multiple memory addresses can map to same cache location
- Management b/w registers & memory: done either by compiler or assembly language programming
- Management b/w cache & main memory: done by the cache controller hardware
	- Abstraction: Do not need to change the program to change the cache layer
- Management b/w main memory & disks (secondary storage): done by operating system (virtual memory). Hardware maps
  virtual to physical adddresses. Exception: programmer can read/write files to memory



