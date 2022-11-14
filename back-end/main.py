# To cross check module: services

import services.api
import json

# For images hosted
face_image_url = 'https://s3.amazonaws.com/s3.mp-cdn.net/12/ce/901b8f87a0314b4f593f0c33597d-is-obama-just-a-really-sad-person.jpg'
face = services.api.face_detect(face_image_url, False)
print(json.dumps(face['emotion']))

# # For images as a stream
# face_image = open('./services/sample_data/img.jpg', 'rb')
# face = services.api.face_detect(face_image, True)

history_all = {'https://medium.com/@curiousblogger/vehicle-detection-using-python-and-opencv-c90b2b0e13d3': {'opencv': 15.329083666734823, 'video': 12.288857529777133, 'python': 8.029604553643358, 'vehicl': 7.938296598989958, 'np.one': 7.411851513676128, 'import': 6.57981695962117, 'detect': 5.102733356067875, 'object': 5.048311300123514, 'cnt': 4.034064046788931, 'line': 4.034064046788931, 'limit': 4.034064046788931, 'imag': 3.648182895592358, 'vision': 3.5606484206366176, 'processor': 3.5606484206366176, 'signal': 3.4812540013687374, 'platform': 3.4500330944091027, 'result': 3.4182868947590093}, 'https://stackoverflow.com/questions/49771659/how-to-filter-hough-lines-for-multi-lane-detection': {'hough': 11.59527655356072, 'multi-lan': 11.59527655356072, 'detect': 11.473033140362448, 'imag': 7.602458924238449, 'filter': 4.944461198346006, 'canni': 4.406712817933873, 'edg': 4.244247386095535, 'houghtransformp': 2.94774878891919, 'output': 2.872317275022549, 'lane': 2.7514754819151537, 'eye': 2.708618007664337, 'view': 2.708618007664337, 'blur': 2.3611031320312126, 'opencv': 1.7545526390187014, 'bird': 1.5519745895857857, 'line': 1.5317321694480128, 'sequenc': 1.5179040005056696, 'step': 1.5179040005056696, 'basic': 1.5179040005056696}, 'https://mindy-support.com/news-post/how-machine-learning-in-automotive-makes-self-driving-cars-a-reality/': {'learn': 45.36426260825813, 'self-driv': 34.5101912033631, 'machin': 30.06927217320395, 'data': 23.58690176063914, 'car': 17.814017502864957, 'automot': 14.385210239923977, 'algorithm': 14.37171604517228, 'realiti': 13.688258314065695, 'object': 11.165355576196987, 'camera': 10.679320964310522, 'sensor': 10.440278444574796, 'interpret': 10.257335288844047, 'make': 9.79433024217228, 'view': 8.996167539940274, 'identifi': 8.945073783892187, 'surround': 8.575711673681726, 'locat': 6.422841781801368}, 'https://comma.ai/': {'introduc': 13.850754011457154, 'comma.ai': 9.668601160075198, 'compat': 4.725102994210803, 'openpilot': 4.6579314925723985, 'regular': 2.4039724370757063, 'comma': 1.8985423597284519, 'dozen': 1.8985423597284519, 'model': 1.8985423597284519, 'ad': 1.8985423597284519, 'check': 1.6167345505972528, 'complet': 1.6167345505972528, 'list': 1.6167345505972528, 'carscompat': 1.6167345505972528, 'car': 1.575034331403601}, 'https://www.geeksforgeeks.org/tf-idf-model-for-page-ranking/': {'frequenc': 77.7628341248921, 'document': 75.29123079144148, 'log': 66.50271181013746, 'idf': 49.12455388551743, 'term': 32.277839968100054, 'normal': 30.59386047265928, 'vector': 30.07292802616287, 'comput': 29.8837541766255, 'space': 28.165915833481503, 'number': 26.120815423036422, 'scientist': 24.340869859071738,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     'data': 23.757518786425376, 'represent': 22.74938662506246, 'doc': 21.839029475995684, 'tf-idf': 19.06614297092517, 'similar': 17.72510262516147, 'queri': 14.855088644756048}, 'https://en.wikipedia.org/wiki/Eliezer_Yudkowsky': {'yudkowski': 87.57821630403211, 'intellig': 65.00434152121223, 'edit': 25.28382905628267, 'system': 24.179828957138156, 'artifici': 21.85402219916004, 'ration': 19.179068472843912, 'russel': 18.18086215683466, 'miri': 18.075593725616653, 'norvig': 16.684515289422137, 'harri': 14.63326307568109, 'research': 14.053512212823945, 'eliez': 12.52533078428843, 'goal': 11.468469425839924, 'institut': 11.272734744144989, 'explos': 11.154389348100802, 'overcom': 11.130587747624945, 'bias': 11.130587747624945, 'friend': 11.12529156881057, 'potter': 10.38692657570214, 'work': 9.053533233915116}, 'https://stackoverflow.com/questions/29351840/stack-two-pandas-data-frames/29351948': {'hzdept': 17.54084886409434, 'hzdepb': 14.778087579916415, 'sandtot': 14.778087579916415, 'stack': 9.325398571722943, 'panda': 9.325398571722943, 'frame': 8.415998480886895, 'data': 7.128924364369337, 'datafram': 5.5865788205439175, 'result': 3.1352890134137477, 'horizont': 3.1352890134137477, 'vertic': 3.1352890134137477, 'give': 2.764701663978304, 'merg': 2.764701663978304, 'oper': 2.764701663978304, 'work': 2.764701663978304, 'line': 2.764701663978304}, 'https://stackoverflow.com/questions/30975339/slicing-a-python-ordereddict': {'getitem': 23.991831983268394, 'slicableordereddict': 17.781199485223254, 'ordereddict': 17.45159440499576, 'python': 13.78113116185656, 'print': 12.192173058752527, 'return': 10.725359045497939, 'odict': 10.241231814680376, 'order': 7.317536094006927, 'ruamel.ordereddict': 7.178782986348636, 'standard': 5.93981018852491, 'function': 5.93981018852491, 'import': 5.907493009469641, 'def': 5.879232331477091, 'k.stop': 5.879232331477091, 'slice': 5.50697101326719, 'key': 5.3840872397614765, 'librari': 5.25604147811976, 'isinst': 5.06507245943869, 'dict': 4.735979297586742}, 'https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string': {'html': 13.377571775537332, 're.compil': 7.931069821737402, 'cleanr': 7.638658684152984, 'beautifulsoup': 7.150060432030654, 'raw': 6.2533801666645425, 'regex': 5.9687415578579115, 'python': 5.469028979774896, 'string': 5.469028979774896, 'lxml': 5.035679307740498, 'cleantext': 4.877462483519439, 'import': 4.315587577883214, 'code': 4.2833682300386995, 'remov': 4.2833682300386995, 'tag': 4.2833682300386995, 'text': 3.2865131627065503, 'addit': 3.191900402657913, 'recommend': 3.1858122295861317, 're.sub': 2.8529457157061935, 'nsbm': 2.8529457157061935, 'insid': 2.286767858129301}}
history_just = {'https://azure.microsoft.com/en-in/services/cognitive-services/face/': {'republ': 1390.1175749754998, 'territori': 111.50700198278142, 'saint': 82.21457121751322, 'island': 73.97581892531608, 'state': 53.95050996145853, 'depart': 51.942349729063785, 'democrat': 51.110685863848744, 'kingdom': 51.110685863848744, 'oversea': 51.110685863848744, 'unit': 50.30552879106491, 'collect': 38.84069850026986, 'south': 35.24065481120412, 'guinea': 23.686766455527202, 'countri': 20.2542478317958, 'region': 20.2542478317958, 'recognit': 17.389593099079796, 'bailiwick': 13.506827369787404, 'virgin': 13.506827369787404}, 'https://medium.com/@curiousblogger/vehicle-detection-using-python-and-opencv-c90b2b0e13d3': {'opencv': 15.329083666734823, 'video': 12.288857529777133, 'python': 8.029604553643358, 'vehicl': 7.938296598989958, 'np.one': 7.411851513676128, 'import': 6.57981695962117,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'detect': 5.102733356067875, 'object': 5.048311300123514, 'cnt': 4.034064046788931, 'line': 4.034064046788931, 'limit': 4.034064046788931, 'imag': 3.648182895592358, 'vision': 3.5606484206366176, 'processor': 3.5606484206366176, 'signal': 3.4812540013687374, 'platform': 3.4500330944091027, 'result': 3.4182868947590093}, 'https://becominghuman.ai/a-simple-introduction-to-natural-language-processing-ea66a1747b32': {'natur': 88.52695978672934, 'process': 70.30781279946427, 'nlp': 56.78721691486058, 'involv': 48.17788182534199, 'languag': 29.339680417454957, 'human': 23.398698272517464, 'word': 22.707181754972243, 'text': 21.239062004449522, 'sentenc': 20.07846952861056, 'analysi': 17.845275960986783, 'understand': 17.77930952196125, 'mean': 15.005874404109749, 'rule': 10.551452585955229, 'comput': 10.332450760714629, 'grammat': 10.17936197869988, 'machin': 8.626587943047406}}


print(services.api.detect_change(history_all, history_just))
