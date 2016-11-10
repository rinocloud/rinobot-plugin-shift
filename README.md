# rinobot-plugin-shift

Shifts an axis of your data by some number.

If your data looks like:

```
0.0 8
1.4 2
2.4 2
3.3 3
4.1 7
...
...
```

And you choose to shift the second column by -1 then the result will be:

```
0.0 7
1.4 1
2.4 1
3.3 2
4.1 6
...
...
```


## Arguments:

In the extra args section of the rinobot automation config you can set the following parameters

- shift [__required__]: the number to shift the data by
- cols: the columns to work on (see [Selecting columns and rows of data](https://docs.rinocloud.com/rinocloud-desktop/slicing_data.html))
