#安裝UI小工具模組
#!pip install ipywidgets
#https://ipywidgets.readthedocs.io/en/latest/index.html

#導入UI小工具模組
import ipywidgets as widgets #導入元件
from IPython.display import display #顯示元件

#選擇物種類別
dd1 = widgets.Dropdown(
    # options=[('請選擇', 0), ('動物 (推薦)', 10), ('植物', 20), ('真菌', 30), ('細菌', 40), ('病毒', 50)],
    options=[('請選擇', 0), ('動物 (推薦)', 10),],
    value=0,
    description='物種類別 ',
)
#選擇序列種類
dd2 = widgets.Dropdown(
    # options=[('請選擇', 0), ('RNA', 10), ('DNA (推薦)', 20), ('mRNA', 30), ('Proteins', 40), ('Glycans', 50), ('Lipids', 60)],
    options=[('請選擇', 0), ('DNA (推薦)', 20), ('mRNA', 30), ('Proteins', 40),],
    value=0,
    description='序列種類',
)
#確認取值按鈕
btn1 = widgets.Button(description="確 認", button_style='success')

species_type = ''
sequence_type = 'ABC'

def btn1_click(b):
  global species_type, sequence_type
  species_type = type_to_name('species', dd1.value)
  sequence_type = type_to_name('sequence', dd2.value)
  output.value = f"您目前點選 {species_type} 和 {sequence_type} 。"
  print(output.value)
  if dd1.value == 10 and dd2.value >=20 and dd2.value <= 30:
    print(f"成功選取 {dd1.value}_{species_type} 和 {dd2.value}_{sequence_type}！")
  else:
    print("請重新選取！")

def type_to_name(sort, code):
  if sort == 'species':
    match code:
      case 10: name = '動物'
      case 20: name = '植物'
      case 30: name = '真菌'
      case 40: name = '細菌'
      case 50: name = '病毒'
      case _: name = '(未知)'
  elif sort == 'sequence':
    match code:
      case 10: name = 'RNA'
      case 20: name = 'DNA'
      case 30: name = 'mRNA'
      case 40: name = 'Proteins'
      case 50: name = 'Glycans'
      case 60: name = 'Lipids'
      case _: name = '(未知)'
  return name

# #按鈕監聽取值
# btn1.on_click(btn1_click)

# output = widgets.Output()

# print('請先選擇物種類別、序列種類\n')
# display(dd1, dd2)
# print()
# display(btn1)
# print()
# display(output)