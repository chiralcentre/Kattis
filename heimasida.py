domain = input().strip()
# remove non alphanumeric characters
domain = ''.join(char for char in domain if char.isalnum())
# all accented characters lose their accent
mappings = {'Á': 'A', 'á': 'a', 'Ð': 'D', 'ð': 'd', 'É': 'E',
            'é': 'e', 'Í': 'I', 'í': 'i', 'Ó': 'O', 'ó': 'o',
            'Ú': 'U', 'ú': 'u', 'Ý': 'Y', 'ý': 'y', 'Þ':'TH',
            'þ': 'th', 'Æ': 'AE', 'æ': 'ae', 'Ö': 'O', 'ö': 'o'
            }
domain = ''.join(mappings.get(char,char) for char in domain)
# make domain lower case
print(domain.lower() + ".is")
