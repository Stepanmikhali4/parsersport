from Parser_class import Parser

parser = Parser('https://www.sport-express.ru/news/', 'news1.txt')

parser.run()
print(parser.results)
