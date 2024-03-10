# Longest Common Prefix Finder

This is a Python program to find the longest common prefix among a list of strings. It provides two methods to achieve this:

## Method 1:

- **String slicing with no recursion**
- **Time Complexity:** 10 ms
- **Space Complexity:** 11.83 MB

## Method 2:

- **Recursive call with reducing the longest prefix**
- **Time Complexity:** 20 ms
- **Space Complexity:** 20 MB

## Usage:

### Predefined Lists of Strings

If you want to use predefined lists of strings, choose option 1 when prompted. Example:

```python
temp = ["brinjal", "bright", "bring"]
```

### Enter Your Own List of Strings

If you want to enter your own list of strings, choose option 2 when prompted. Example:

```python
temp = ["string1", "string2", "string3"]
```

## How to Run

### Clone the repository 
```
git clone https://github.com/Phaneesh-Katti/upgraded-broccoli.git
cd your-repo
```

### Run the Program
```
python longest_prefix.py
```

<br><br>
## Example
This is a program to find the longest common prefix among a list of strings. 
For example, the following list: 
  flower, flow, flight 
has 'fl' as the longest common prefix.

Enter 1 if you want to use predefined lists of strings. 
Enter 2 if you want to enter your list of strings. 
Your choice: 1

Method 1:

String slicing + no recursion

Time: 10 ms

Space: 11.83 MB

Item list: ['brinjal', 'bright', 'bring']

Longest common prefix: bri

<br>

Method 2:

Recursive call with reducing the longest prefix

Time: 20 ms

Space: 20 MB

Item list: ['brinjal', 'bright', 'bring']

Longest common prefix: bri

<br>


## Contributing
Feel free to contribute by opening issues or creating pull requests.

## License
This project is licensed under the MIT License.
