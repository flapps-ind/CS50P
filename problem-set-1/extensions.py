def main():
  x = input("File name: ").strip().lower()
  fileName = x.rsplit('.', 1)[1]
  match fileName: 
    case "jpg" | "jpeg":
      print("image/jpeg")
    case "gif":
      print("image/gif")
    case "png":
      print("image/png")
    case "pdf":
      print("application/pdf")
    case "txt":
      print("application/txt")
    case "zip":
      print("application/zip")
    case _:
      print("application/octet-stream")         

main()      
