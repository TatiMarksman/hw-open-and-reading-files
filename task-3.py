def merged_files(file_list, output_file):
  files_content = []

  for fname in file_list:
      with open(fname, 'r', encoding='utf-8') as f:
          content = f.readlines()
          files_content.append((len(content), fname, content))

  files_content.sort()

  with open(new_file, 'w', encoding='utf-8') as f:
      for lines_count, fname, content in files_content:
          f.write(f'\n{fname}\n')
          f.write(f'{lines_count}\n')
          f.writelines(content)

file_list = ['1.txt', '2.txt', '3.txt']
new_file = 'merged_all.txt'

merged_files(file_list, new_file)