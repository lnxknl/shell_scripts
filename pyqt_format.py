import sys                                                                            
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton
                                           
class TextFormatter(QWidget):                                                         
    def __init__(self):                                                               
        super().__init__()                                                            
        self.initUI()                      
                                          
    def initUI(self):                     
        layout = QVBoxLayout()             
                                           
        self.input_text = QTextEdit()      
        self.input_text.setPlaceholderText("Enter text with '\\n' for newlines")
        layout.addWidget(self.input_text)  
                                           
        self.format_button = QPushButton("Format Text")
        self.format_button.clicked.connect(self.format_text)
        layout.addWidget(self.format_button)
                                                                                      
        self.output_text = QTextEdit()     
        self.output_text.setReadOnly(True)                                            
        layout.addWidget(self.output_text)                                                                                                                                  
                                                                                      
        self.setLayout(layout)                                                        
        self.setWindowTitle('Text Formatter')
        self.setGeometry(300, 300, 400, 300)                         
                                                                                      
    def format_text(self):                                                            
        input_text = self.input_text.toPlainText()   
        formatted_text = input_text.replace("\\n", "\n")
        self.output_text.setPlainText(formatted_text)                                                                                                                       

if __name__ == '__main__':                                                                                                                                                  
    app = QApplication(sys.argv)                                                                                                                                            
    formatter = TextFormatter()            
    formatter.show()                       
    sys.exit(app.exec_())                  
