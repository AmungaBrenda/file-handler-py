# file-handler-py

 A beginner-friendly Python project that reads a text file, modifies its content, and writes the results to a new file — all while handling errors gracefully.
 A Python utility for safely reading, modifying, and writing text files with comprehensive error handling.

## 🌟 Features

- **User-friendly Interface**: Simple command-line interaction for file operations
- **Comprehensive Error Handling**: Gracefully manages various file-related exceptions
- **File Transformation**: Converts file content to uppercase (easily customizable)
- **Overwrite Protection**: Safeguards against accidental file overwrites
- **File Statistics**: Reports character counts for original and modified files
- **Multi-file Processing**: Option to process multiple files in succession

## 📋 Requirements

- Python 3.6+
- No external dependencies required

## 🚀 Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/AmungaBrenda/file-handler-py.git
cd file-handler-py
```

## 💻 Usage

Run the program with Python:

```bash
python file_processor.py
```

Follow the interactive prompts:
1. Enter the name of the file you want to read
2. Specify the output filename for the modified version
3. Confirm overwrite if the output file already exists
4. Choose whether to process another file when done

## 🔍 Error Handling

The utility handles various scenarios including:
- Non-existent input files
- Permission errors (read/write)
- Non-text files (encoding issues)
- I/O errors during reading/writing
- User cancellation on overwrite prompts

## 🛠️ Customization

To modify how files are transformed, edit the `process_file()` function in `file_processor.py`. 

The current transformation converts text to uppercase:

```python
# Modify the content (example: convert to uppercase)
modified_content = content.upper()
```

You can replace this with any text transformation logic you need.

## 📝 Example

```
File Modification Program
-------------------------
Enter the name of the file to read: sample.txt
Enter the name for the modified output file: sample_modified.txt
Success! Modified content written to 'sample_modified.txt'.
Original file size: 152 characters
Modified file size: 152 characters

Process another file? (y/n): n
Thank you for using the File Modification Program!
```

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Contact

If you have any questions or feedback, please open an issue on this repository.

---

⭐ If you find this project useful, please consider giving it a star on GitHub! ⭐
