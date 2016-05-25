import CommonMark

parser = CommonMark.Parser()
renderer = CommonMark.HtmlRenderer()

ast = parser.parse("Hello *World*")
html = renderer.render(ast)
# json = CommonMark.ASTtoJSON(ast)

# CommonMark.dumpAST(ast)
print(html)


# with syntactic sugar
myhtml = CommonMark.commonmark("Hello *goodbye* I see *I try*!")
print(myhtml)
