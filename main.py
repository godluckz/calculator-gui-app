from PySide6.QtWidgets import (QApplication, 
                               QMainWindow, 
                               QPushButton, 
                               QLineEdit,
                               QGridLayout,
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
                    "🆑": self._clear,
                   "🟰": self._equal
                    }
        
        # self.operations = {            
        #             "🆑": self._clear,
        #             "+-": self._change_sign,
        #             "%": self._percent,            
        #             "+": self._add,
        #             "-": self._subtract,
        #             "x": self._multiply,
        #             "/": self._divide,
        #            "🟰": self._equal
        #             }
        
        self._initialize()    

        self._add_buttons()


    def _add_display(self) -> None:

        self.screep_display = QLineEdit()
        self.screep_display.setPlaceholderText("0")
        self.screep_display.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.screep_display.setReadOnly(True)    
        self.screep_display.setFixedSize(230,55)

        self.screep_display.setStyleSheet("""
                                    QLineEdit {
                                            font-size: 40px;
                                            padding: 0 10 0 0;
                                            qproperty-alignment: AlignRight;
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
        pressed_button_det = pressed_button.text()
        if pressed_button_det in ("🆑","🟰"):
            if pressed_button_det == "🟰":                  
                self._process_user_input()        
            self.operations[pressed_button_det]() #Process equal
        else:
            self.user_input.append(pressed_button_det)
            self.temp_disp_value  = f"{self.temp_disp_value }{pressed_button_det}"
            self._set_diplay(self.temp_disp_value )
        
        self.last_click = pressed_button_det


    #Calculator functions below
    def _initialize(self) -> None:
        '''Intialize calculator'''
        self.result = None    
        self.last_click = None            
        self.user_input      = []
        self.temp_disp_value  = ""


    def _clear(self) -> None:
        '''Clear Screen and intialize calculator'''
        self.screep_display.clear()      
        self._initialize()


    def _change_sign(self, p_num) -> float:
        '''Change Sign'''        
        return float(p_num) * -1        
    

    def _equal(self) -> None:
        w_result = self.result
        if w_result:
            w_result = round(w_result,4)
        self._set_diplay(w_result)
        self._initialize()   
        

    def _set_diplay(self, p_text: str) -> None:
        self.screep_display.setText(str(p_text))
    

    def _process_user_input(self):
        w_math_input_list = []
        w_val             = ""

        for index, i in enumerate(self.user_input):    
            if i.replace(".","").isnumeric() or i in ("%","."): #isnumeric doesnt work with float.. remove . first
                w_val = f"{w_val}{i}"   
                if index == len(self.user_input)-1:                    
                    w_math_input_list.append(w_val) #last element
                else:
                    continue #check next item first                           
            else:        
                w_math_input_list.append(w_val)
                w_math_input_list.append(i)
                w_val = ""                    

        # Apply operator to the previous result and the current number
        w_sub_result = float(w_math_input_list[0])

        prev_num = w_sub_result          
        for i in range(1, len(w_math_input_list), 2):
            w_number = None
            w_is_prct = False
            operator = w_math_input_list[i]

            try:
                w_number = w_math_input_list[i+1]
                if "%" in w_number:
                    w_is_prct = True
                    w_number = w_number.replace("%","")
                
                if w_number.replace(".","").isnumeric():#isnumeric doesnt work with float.. remove . first
                    w_number = float(w_number)
                    prev_num = w_number
            except Exception as e:            
                w_sub_result = None
        
            if operator and w_number:
                if w_is_prct:
                    w_sub_result_pct = (w_number / 100) * w_sub_result
                    w_sub_result = w_sub_result + w_sub_result_pct
                elif operator == '+':
                    w_sub_result += w_number
                elif operator == '-':
                    w_sub_result -= w_number
                elif operator in ('*','x'):
                    w_sub_result *= w_number
                elif operator == '/':
                    w_sub_result /= w_number
        
        self.result = w_sub_result
        


def main() -> None:   
    from sys import argv
    W_APP = QApplication(argv)
    W_WINDOW = Calculator()     
    W_WINDOW.show()
    W_APP.exec()    


if __name__ == "__main__":
    main()