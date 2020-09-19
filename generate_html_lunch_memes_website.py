from os import listdir

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        if n[-1] == '.':
            return False
        return True

num_memes = 218
files = [f for f in listdir()]
sorted_memes = [None] * (num_memes + 1)
string = 'lunch meme '
for meme in files:
    if meme[:len(string)] == string:
        i = 1
        while is_integer(meme[len(string): len(string) + i]):
            num = int(meme[len(string): len(string) + i]) 
            i += 1
        sorted_memes[num] = meme
sorted_memes = [i for i in sorted_memes if i != None]

        
f = open('website_lunch_memes.html', 'w+')


f.write(
'<!DOCTYPE html>\n' + 
'<html>\n' +
'<meta charset="UTF-8">\n' +
'<meta name="viewport" content="width=1000, intial-scale=1">\n' +
'<link rel="stylesheet" href="https://www.w3schools.com/w3css/3/w3.css">\n' +
'<body>\n\n'
)


f.write(
'<!-- Website Title -->\n' + 
'<section class="w3-container w3-center" style="max-width:600px">\n' +
'  <p class="w3-opacity"><i>The eternal resting place of</i></p>\n' +
'  <h2 class="w3-wide">Lunch Memes</h2>\n' +
'</section>\n\n'
)

f.write(
'<!-- Slide Show -->\n' +
'<section class="w3-container w3-center" style="max-width:600px">\n'
)

for meme in sorted_memes:
    if meme != None:
        if meme.endswith('.jpg') or meme.endswith('.png'):
            f.write(
            '  <img class="mySlides" src="'+meme+'" style="width:100% ">\n'
            )

f.write(
'</section>\n\n' +
'<script>\n' +
'// Automatic Slideshow - change image very 3 seconds\n' + 
'var myIndex = 0;\n' +
'carousel();\n\n'
)

f.write(
'function carousel() {\n' +
'  var i;\n' +
'  var x = document.getElementsByClassName("mySlides");\n' +
'  for (i = 0; i < x.length; i++) {\n' +
'    x[i].style.display = "none";\n' +
'  }\n' +
'  myIndex++;\n' +
'  if (myIndex > x.length) {myIndex = 1}\n' +
'  x[myIndex-1].style.display = "block";\n' +
'  setTimeout(carousel, 3000);\n' +
'}\n' + 
'</script>\n\n'
)


row = 1
i = 0
while i < len(sorted_memes):
    f.write(
    f'<!-- Names and Photos Row {row} -->\n' +
    '<section class="w3-row-padding w3-center w3-light-grey" style="max-width:100%">\n'
    )
    for _ in range(4):
        if i < len(sorted_memes):
            f.write(
            '<article class="w3-quarter">\n' +
            f'    <p>Lunch Meme {i + 1}</p>\n' + 
            '    <img src="'+sorted_memes[i]+'" alt="Random Name" style="width:100%">\n' +
            '</article>\n'
            )
            i += 1
    f.write(
    '</section>\n\n'
    )
    row += 1

f.write(
'</body>\n' +
'</html>'
)

f.close()