## 1. Introduction ##

lyrics = ' white lips, pale face \n breathing in snowflakes'
print(lyrics)

## 3. Splitting a string into a list ##

lyrics = ' white lips, pale face \n breathing in snowflakes \n burnt lungs sour taste \n lights gone days end \n struggling to pay rent \n long nights strange men \n and they say \n shes in the class a team \n stuck in her daydream \n been this way since 18 \n but lately her face seems  \n slowly sinking wasting \n crumbling like pastries \n they scream \n the worst things in life come free to us \n cause were just under the upperhand \n and go mad for a couple grams \n and she dont want to go outside tonight \n and in a pipe she flies to the motherland \n or sells love to another man \n its too cold outside \n for angels to fly \n angels to fly \n ripped gloves raincoat \n tried to swim stay afloat \n dry house wet clothes \n loose change bank notes \n wearyeyed dry throat \n cool girl no phone \n and they say \n shes in the class a team \n stuck in her daydream \n been this way since 18 \n but lately her face seems \n slowly sinking wasting \n crumbling like pastries \n and they scream \n the worst things in life come free to us \n cause were just under the upperhand \n and go mad for a couple grams \n but she dont want to go outside tonight \n and in a pipe she flies to the motherland \n or sells love to another man \n its too cold outside \n for angels to fly \n an angel will die \n covered in white \n closed eye \n and hoping for a better life \n this time well fade out tonight \n straight down the line \n and they say \n shes in the class a team \n stuck in her daydream \n been this way since 18 \n but lately her face seems \n slowly sinking wasting \n crumbling like pastries \n they scream \n the worst things in life come free to us \n and were all under the upperhand \n go mad for a couple grams \n and we dont want to go outside tonight \n and in a pipe we fly to the motherland \n or sell love to another man \n its too cold outside \n for angels to fly \n angels to fly \n to fly fly \n for angels to fly to fly to fly \n angels to die'

a_team = lyrics.split("\n")

## 4. Changing the values of an immutable object ##

ed_sheeran = [list(i) for i in a_team]

## 5. Uppercasing And Lowercasing Strings ##

for i in ed_sheeran:
    i[1] = i[1].upper()
print(ed_sheeran)

## 6. Joining a list of strings into one string ##

ed_sheeran = ["".join(i) for i in ed_sheeran]
ed_sheeran_full = "\n".join(ed_sheeran)

## 7. String Concatenation ##

ed_sheeran_full = ''
for i in ed_sheeran:
    ed_sheeran_full += i +"\n"
print(ed_sheeran_full)

## 8. Replacing Values In A String ##

mad_libs_joined = "\n".join(mad_libs)
mad_libs_joined = mad_libs_joined.replace("{ADJ}", "stinky")
mad_libs_joined = mad_libs_joined.replace("{NOUN}", "piano")
mad_libs_joined = mad_libs_joined.replace("{AGE}", "99")
mad_libs_joined = mad_libs_joined.replace("{NOUN_PLURAL}", "phones")
mad_libs_joined = mad_libs_joined.replace("{VERB}", "crush")
mad_libs_joined = mad_libs_joined.replace("{LOCATION}", "Antarctica")
mad_libs_joined = mad_libs_joined.replace("{CELEBRITY}", "Beyonce")

## 9. Replacing Values In A String Using Formatter ##

"White lips, pale face"
first_line = "White {0}, pale {1}".format("hat","skin")

## 10. Formatting our song lyrics ##

final = mad_libs.format(ADJ ="strong",NOUN ="piano",AGE = "99",NOUN_PLURAL="phones",VERB="smash",LOCATION="Antarctica",CELEBRITY="Beyonce")   