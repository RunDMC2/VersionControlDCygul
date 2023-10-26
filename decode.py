def decode(password):
  decodedPW = ""
  for i in range(len(password)):
    decodedPW += str((int(password[i]) - 3)%10)
  return decodedPW
