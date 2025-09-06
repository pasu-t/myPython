Iteratable: something cab be looped over but more sepcifically an object needs to return an iterator object from its magic method(dunder method) and the iterator that is returned from the dunder method must define a dudner next method which accesses elements the container one at a time.

-->So just because something is iterable doesn't mean that it is an iterator

-->Iterator means that it's a object with a state so that it remembers where it's at during its iteration and it knows how to fetch next value using dunder next method.