### 0x0B. Python - Input/Output (read file and write to file)
** Python File Methods **
| Method | What it does |
| ------ | ------------ |
| close() | Closes the file. |
| flush() | Flushes the internal buffer. |
| fileno() | Returns the file descriptor of the file. |
| next() | Returns the next line from the file. |
| read(size) | Reads size number of bytes from the file.
Reads the entire file if you don’t pass any argument value. |
| readline(size) | Reads one line from a file. |
| readlines() | Reads the entire file and returns a list of the lines. |
| seek(offset, whence) | Lets us control the position of the file pointer. |
| tell() | Returns the current position of the file pointer. |
| truncate(size) | It truncates the file to the specified size. |
| writable() | Returns True if we can write into the file. |
| write(string) | Writes string into the file. |
| writelines(list_of_strings) | Writes each element of the list_of_strings
into the file. |