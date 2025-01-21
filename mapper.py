from flask import Flask, render_template, url_for, request
from translate_shell.translate import translate

app = Flask(__name__)


# return index page which renders world map
@app.route('/', methods=['POST', 'GET'])
def index():
	wordsToMap = {}
	if request.method == 'POST':
		translateWord = request.form['translationWord']
		translateLang = request.form['langSelect']

		if translateWord != '':
			wordsToMap = processTranslations(translateLang,translateWord)
			print(wordsToMap)
	return render_template('world.html', data=wordsToMap)

@app.route('/africa/')
def africaMap():
	return render_template('africa.html')


@app.route('/asia/')
def asiaMap():
	return render_template('asia.html')


@app.route('/india/')
def indiaMap():
	return render_template('india.html')


@app.route('/europe/')
def europeMap():
	return render_template('europe.html')
	return results

# requires: language we are translating from, phrase to translate
# effects: returns a dict of all the translations
def processTranslations(source_lang, phrase):
	print("starting process Translations with" , source_lang, phrase)
	results = dict()
	listOfLangsToTranslateInto = resolveLang(source_lang, 'world')
	for lang in listOfLangsToTranslateInto:
		translationItem = translate(phrase, lang)
		results[lang] = translationItem.results[0].paraphrase
	return results
 
# returns: tupple with first value being what map we are projecting on, second being language list
def resolveLang(langIn, map):
	assert langIn != '', "langIn should not be empty"
	assert map != '', "langIn "

	if map == 'africa':
		langList = list(["AF", "AR", "SW", "XH"])

	if map =='asia':
		langList = list(["AF", "AR", "BN", "KH", "ZH", "FJ", "KA", \
		"GU", "HI", "ID", "JA", "JW", "KO", "MS", "ML", "MR" \
		"MN", "NE", "FA", "PA", "PA", "SM", "TA", "TE", "TH" \
		"BO", "TO", "TR", "UR", "UZ", "VI"])

	if map == 'europe':
		langList = list(["SQ", "EU", "BG", "BG", "CA", "HR", \
		"CS", "DA", "NL", "EN", "ET", "FI", "FR", "DE", "EL", \
		"HU", "IS", "GA", "IT", "LA", "LV", "LT", "MK", "MT", \
		"NO", "PL", "PT", "RO", "RU", "SR", "SK", "SL", "ES", \
		"SV", "TT", "UK", "CY" ])

	if map == 'india':
		langList = list(["BN", "ZH", "GU", "HI", "ML", \
		"MR", "NE", "FA", "PA", "TA", "TE", "BO", "URs"])

	if map == 'world':
		langList = list(["AF", "AR" ,"SQ", "HY", "EU", "BN", "BG", "CA", "KM", "ZH", "HR", "CS", "DA", "NL", "EN", "ET", "FJ"\
	, "FI", "FR", "KA", "DE", "EL", "GU", "HE", "HI", "HU", "IS", "ID", "GA", "IT", "JA", "JW", "KO", "LA", "LV", "LT"\
	, "MK", "MS", "ML", "MT", "MI", "MR", "MN", "NE", "NO", "FA", "PL", "PT", "PA", "QU", "RO", "RU", "SM", "SR", "SK", "SL"\
	, "ES", "SW", "SV", "TA", "TT", "TE", "TH", "BO", "TO", "TR", "UK", "UR", "UZ", "VI", "CY", "XH"])

	langList.remove(langIn)
	return langList

# start function for app
if __name__=="__main__":
	app.run(debug=True)