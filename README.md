# ansible-multi-inventory-demo
This is a quick demonstration of using different inventory plugins and group hosts together using simple hostname patterns.

There are two dummy plugins providing hosts with different pattern, a static host file and constructed plugin


```
$ ansible-inventory -i demo-inventory-dir -vvvv --graph

