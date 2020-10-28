# Técnicas Criptográficas - Advanced Encryption Standard

message = 'Man request adapted spirits set pressed. Up to denoting subjects sensible feelings it indulged directly.'

round_key = (
  0x63, 0xa4, 0x12, 0x14,
  0x41, 0xf3, 0x27, 0x12,
  0x8C, 0xA1, 0x89, 0x0D,
  0xE6, 0x42, 0x68, 0x41,
)

def textToMatrix(text):
  matrix_group = [] 
  matrix_counter = 0
  hex_text = (text.encode(encoding="utf-8")).hex()
  hex_start = 0
  hex_end = 0

  if len(text) > 128:
    raise Exception('Message range exceed the 128 char limit')

  while hex_end < len(hex_text):
    matrix = []
    hex_start = 32 * matrix_counter
    hex_end = 32 * (matrix_counter + 1)
    hex_piece = hex_text[hex_start:hex_end]
    
    for i in range(16):
      hex_char = hex_piece[2 * i: 2 * (i + 1)]
      matrix.append(hex_char or '00')

    matrix_counter += 1
    matrix_group.append(matrix)

  return matrix_group

def addRoundKey(group, key):
  matrix_group = []
  for matrix in group:
    matrix_key = []
    for i in range(16):
      matrix_key.append(int(matrix[i], base=16) ^ key[i])
      
    matrix_group.append(matrix_key)

  return matrix_group

def substituteBytes():
  pass

def shiftRows():
  pass

def mixColumns():
  pass

def crypt():
  pass

def decrypt():
  pass

matrix_group = textToMatrix(message)
matrix_group_key = addRoundKey(matrix_group, round_key)
