from PySide6.QtWidgets import (QApplication, 
                               QMainWindow, 
                               QPushButton, 
                               QLineEdit,
                               QGridLayout,
                               QLabel, 
                               QWidget)
from PySide6.QtCore import Qt


class Calculator(QMainWindow):
    def __init__(self,):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(1600,100,230,290)
        self.setFixedSize(230, 290)
        self.setWindowOpacity(0.99)
        self.setStyleSheet("""
                            background-color: rgb(61,62,59);
                            color: white;
                           """)
              

        self.layout  = QGridLayout()     
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        
        _central_widged = QWidget()
        _central_widged.setLayout(self.layout)
        self.setCentralWidget(_central_widged)
        self._add_display()

        self.layout.addWidget(self.screep_display,0,0,1,4)        


        self.operations = {            
                    "c": self._clear,
                    "+-": self._change_sign,
                    "%": self._percent,            
                    "+": self._add,
                    "-": self._subtract,
                    "*": self._multiply,
                    "/": self._divide,
                    "=": self._equal
                    }
        self.result = None
        self.num1   = None
        self.num2   = None
        self.operator = None

        self._add_buttons()


    def _add_display(self) -> None:

        self.screep_display = QLineEdit()
        self.screep_display.setPlaceholderText("0")
        self.screep_display.setReadOnly(True)
        self.screep_display.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.screep_display.setFixedSize(230,55)
        # self.screep_display.setStyleSheet("""
        #                                     QLineEdit {
        #                                         font-size: 40px;
        #                                         padding: 0 20 0 0;
        #                                     }
        #                                     """)
        self.screep_display.setStyleSheet("""
                                    QLineEdit {
                                        font-size: 40px;
                                        padding: 0 10 0 0;
                                        font-weight: 200;
                                            background: qlineargradient(
                                                x1: 0, y1: 0,
                                                x2: 0, y2: 1,
                                                stop: 0 rgb(58, 58, 62),
                                                stop: 0.6 rgb(58, 59, 62),
                                                stop: 1 rgb(52, 68, 80)
                                            );
                                    }
                                    """)        
        

    def _add_buttons(self) -> None:
        self.buttons = [
            "🆑", "+-", "%", "+",
            "7", "8", "9", "x",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "🟰"                        
        ]
       
        width = 60
        height = 50

        row = 0
        col = 0

        for r_btn in self.buttons:
            _btn  = QPushButton(r_btn)
            _btn.pressed.connect(self._button_clicked)

            num_columns = 1
            row_offset  = 1
            col_offset  = 0
            if row == 4: #move everything to the right except 0, and give 0 two columns
                if r_btn == "0":
                    num_columns += 1
                else:
                    col_offset = 1            

            self.layout.addWidget(_btn,row+row_offset,col+col_offset,1,num_columns)
            _btn.setFixedSize(width*num_columns, height)
            col+=1
            col_offset = 0

            if r_btn == "🆑":
               _btn.setStyleSheet("""
                                    background-color:rgb(144, 238, 144);
                                    color:red
                                  """)
            elif r_btn == "🟰":
                _btn.setStyleSheet("""
                                    background-color:rgb(144, 238, 144)
                                  """)

            if col > 3: #4+ move to the next row
                row+=1
                col = 0
            

    def _button_clicked(self) -> None:
        pressed_button = self.sender()
        pressed_button_text = pressed_button.text()
        print(pressed_button_text)


    def _clear(self) -> None:
        self.screep_display.clear()


    def _change_sign(self) -> None:
        raise NotImplementedError


    def _percent(self) -> None:
        raise NotImplementedError
    
    def _add(self) -> None:
        self.result = self.num1 + self.num2


    def _subtract(self) -> None:
        self.result = self.num1 - self.num2


    def _multiply(self) -> None:
        self.result = self.num1 * self.num2


    def _divide(self) -> None:
        self.result = self.num1 / self.num2


    def _equal(self) -> None:
        self.screep_display.setText(str(round(self.result,4)))
        

        

def main() -> None:   
    from sys import argv
    W_APP = QApplication(argv)
    W_WINDOW = Calculator()     
    W_WINDOW.show()
    W_APP.exec()    


if __name__ == "__main__":
    main()