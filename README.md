[![Wisdomic Panda](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/panda.png)](http://www.rohanbagwe.com/)  **Wisdomic Panda**
> *Hold the Vision, Trust the Process.*


# Beginner's guide to regex in python!
*... a technique to extract and manipulate specific string patterns from a larger texts.*

![Regex](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/reg.gif)

### re turns chaos into order. :sun_with_face:

Regular expressionss, regex, or re are used to identify, replace or delete a string pattern if it exists in a given sequence of characters (strings). They help in manipulating textual data, which is often a pre-requisite for data science projects that involve text mining. Be it extraction of specific parts of text from web pages, making sense of twitter data or preparing your data for text mining – Regular expressions are your best bet for all these tasks.

### :coffee: Ingredients:

- re 
- python
- spyder IDE
- Jupyter Notebook
- Ubuntu 16.4 LTS

## Regex for who?

- **It is widely used in natural language processing, mostly for preprocessing the text.**
- **Web applications that require validating string input (Eg. Email address, Phone number).**
- **Pretty much most data science projects that involve text mining from large data sets.**


## Most commonly used operators:

|**Operator**|**Description**|
|:---:|:---:|
| ^ | start of a string |
| $ | end of a string |
| . |  matches any character, except newline (/n) |
| \ |	 Used to escape a special character |
| ? | Greedily matches expression to its left 0 or 1 times: **Eg.** home-?brew matches either homebrew or home-brew. But if ? is added to qualifiers (+, \*, and ? itself) it will perform matches in a non-greedy manner. |
| a| single character "a"|
| ab | string "ab" |
| **Quantifiers** | |
| + | 1 or more occurrences of the pattern to its left |
|\*| 1 or more occurrences of the pattern to its left \
| {5} |  matches the expression to its left exactly 5 |
| {5, 10} | matches he expression to its left between 5-10 |
| {,5} |  matches he expression to its left upto 5 |
| {2,} |  matches he expression to its left 2 or more |
| **Character Classes** | |
|\s|	 matches a whitespace character  which include the \t, \n, \r, and space characters.|
|\S|	 matches a non-whitespace character|
|\w|	 matches alphanumeric characters, which means a-z, A-Z, and 0-9. It also matches the underscore, \_|
|\W|	 matches a non-word character|
|\d|	 matches one digit 0-9 |
|\D|	 matches one non-digit|
|\A|	matches the expression to its right at the absolute **start of a string** whether in single or multi-line mode. |
| \Z | matches the expression to its left at the absolute **end of a string whether** in single or multi-line mode.|
|\b | matches the word boundary|
|\B|matches Non-word boundary|
|[\b]|	 A backspace character|
|\c|	 A control character|
| **Sets** | |
| [rdb] | Matches either r, d, or b. It does not match rdb.|
|[a-z] | Matches any alphabet from a to z.|
|[a\-z] | Matches a, -, or z. It matches - because \ escapes it.|
|[-a] | As above, matches a or -|
|[a-z0-9] | Matches characters from a to z and also from 0 to 9|
|[(+\*)] | Special characters become literal inside a set, so this matches (, +, \*, and )|
|[^ab5] | Adding ^ excludes any character in the set. Here, it matches characters that are not a, b, or 5|
|**Groups**||
|(ab)\*|matches zero or more repetitions of ab.|
|m = re.match('(a(b)c)d','abcd')|- m.group(0) > 'abcd' - m.group(1) > 'abc' - m.group(2) > 'b'|
|**(?aiLmsux)** | Here, a, i, L, m, s, u, and x are flags|
|a | Matches ASCII only|
|i |Ignore case|
|L | Locale dependent|
|m | Multi-line|
|s | Matches all|
|u | Matches unicode|
|x | Verbose|
| **Special Characters** ||
|\n| Newline|
|\r|	Carriage return|
|\t|	Tab|

> :pushpin: **Greedy: As Many As Possible (longest match)**: 
By default, a quantifier tells the engine to match as many instances of its quantified token or subpattern as possible. This behavior is called greedy. For instance, take the + quantifier. It allows the engine to match one or more of the token it quantifies: \d+ can therefore match one or more digits. But "one or more" is rather vague: in the string 123, "one or more digits" (starting from the left) could be 1, 12 or 123. Which of these does \d+ match? 

> Because by default quantifiers are greedy, \d+ matches as many digits as possible, i.e. 123. For the match attempt that starts at a given position, a greedy quantifier gives you the longest match. 

> #### :warning: **longest match:** it refers to the longest match that can be found with a match attempt that starts at a given position in the string — not to the longest possible match that can be found if a pattern is applied repeatedly to various sections of a string.

### [Source](https://www.rexegg.com/regex-quantifiers.html)

> :pushpin: **Lazy: As Few As Possible (shortest match):**
A lazy (sometimes called reluctant) quantifier tells the engine to match as few of the quantified tokens as needed. As you'll see in the table below, a regular quantifier is made lazy by appending a ? question mark to it. 

> Since the * quantifier allows the engine to match zero or more characters, \w*?E tells the engine to match zero or more word characters, but as few as needed—which might be none at all—then to match an E. In the string 123EEE, starting from the very left, "zero or more word characters then an E" could be 123E, 123EE or 123EEE. Which of these does \w*?E match? 
> Because the *? quantifier is lazy, \w*? matches as few characters as possible to allow the overall match attempt to succeed, i.e. 123—and the overall match is 123E. For the match attempt that starts at a given position, a lazy quantifier gives you the shortest match. 

### [Source](https://www.rexegg.com/regex-quantifiers.html)

## Example:

1. **Grokking Email Address: Regex1**

To extract an email addresses from huge text corpus with regex we need to utilize various tokens. The following regex snippet will match a commonly formatted email address.

	/^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,5})$/

>  ^ to start the string. Then the expression is broken into 3 different groups by '@' and '.'.

- ### Group 1 ([a-z0-9_\.-]+)

Match one or more lowercase letters between a-z, numbers between 0-9, underscores, periods, and hyphens. The expression is then followed by an @ sign.

- ### Group 2 ([\da-z\.-]+) 
 
The domain name must be matched which can use one or more digits, letters between a-z, periods, and hyphens. The domain name is then followed by a period \..

- ### Group 3 ([a-z\.]{2,5})

Matches the top level domain. This section looks for any group of letters or dots that are 2-5 characters long. 



2. **Grokking Email Address: Regex2** 

The same regex can be modified as below depending on the FS:
<img src ="https://github.com/robagwe/wisdomic-panda/blob/master/imgs/eg2.gif" width = "700">

### [Source](https://paulvanderlaken.files.wordpress.com/2017/10/regular-expression.gif?w=371)

#### :construction: Get hands on: [Kick-off](https://github.com/robagwe/kick-off-regex-python/blob/master/cookbook.ipynb)

### ... and then it feels like ...!

<img src ="https://github.com/robagwe/wisdomic-panda/blob/master/imgs/t2.gif" width = "850" height ="400">

## <img src="https://github.com/robagwe/wisdomic-panda/blob/master/imgs/acr.png" width="50">   Hey Buddy!</img>

> This repository explains the rationale for python regex in data preprocessing and Data mining tasks.
I have coded few basic scripts using re module, have a dekko at it! My motive is to get you familiar with the tools that python provides and get you a head start as regex is considered as a heart of data mining. For more details on re, refer [this](https://docs.python.org/2/library/re.html).
If you have any suggestions for more useful regex scripts that should be on this page, let me know or consider submitting a pull request so others can benefit from your work. 
Thank you very much for reaching out! Please follow if you find it handy and hit :star: to get more kick-off repo updates.

:email: [Drop In!!](https://www.rohanbagwe.com) Seriously, it'd be great to discuss Technology.

> *All birds find shelter during a rain. But Eagles avoid rain by flying above the clouds. Problems are common, but attitude make the difference. - A. P. J. Abdul Kalam (*Former President of India*)*

					
