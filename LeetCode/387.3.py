# encoding: utf-8
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = []
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if s.find(c) != -1 and s.find(c) == s.rfind(c):
                result.append(s.find(c))
        if len(result) == 0:
            return -1
        else:
            return min(result)


r = Solution()
print(r.firstUniqChar('leetcode'))
print(r.firstUniqChar('loveleetcode'))
print(r.firstUniqChar('dacca'))
print(r.firstUniqChar(''))
print(r.firstUniqChar('sdnvlbkrmtbollujsdjfjfppksravjkwwsimlmdtcmiilpjibjhcppluisqbqfwrjjlrapsmcwrsrnfrmtjrffpuuqwonqfjfqxellpvmcfmhxccljqlvboioelpfcawrxlwsajfaiehutvogduhobwgpogvatpbvoaognbepqnkhkjsvqmfaghavopppcjbjunuaeotpkbfsmeqikjflakgjexnqqgxnsdjolbjbvhreighxhkihwphexwqufasjakmrdrpwciefaiqsaifmcfdeidhmjekoorvcuxtejlrfscrjekfkcnsdhhsxenhkuanafdpnsjnepdmvvrhbxwuhmrkenrcwbadsiulpvcklhlburudrbbskokwnwqktwjxstsvebvpqcugxjebcivudojorntphtscxhoxlhteuqunhvrsndtabfpdqdcsuqmdbeiiexdkaqtgkncfatlawrudbausifpsicibgrwastcxkjasmrmtrchbwlkxnbsxeaurtfdwmjqkgikcctgccsisgwlkkwflvahasltfusxogtbejrderxbqshacgsrvtqpgdcwmuwuejcmqanirwthsaxihlowgwjeegdltsujtrfuhjnqjjefqjwubiktuglirmgcdqfolvmrilkrvtlrtntujffbrtfiwdtvtfrkfnwklfulecxtkvqpgcrqvgjxbebjlbiopbnhqbdhhxsmgpdojhupxnfkmqsjlmcserhsiwhvelcufuvqrvpwhckexvutuwgfbgnqsmpmfuqkrvwggskovlqtqnqxvpghqoomplnnkmuhkbwpaxuhrkphbgwopxikisuegmxhbjocwhumauhiegojccvibwfdrdnahnwduvnuxjcuncrcgwwrjhxmdemnuxcjspjisgduuoojpxluvehoqpctncxniatxqckhmggtwgjihfnxdhbjwjhuqwuoveibqppqrmxrmaddukgcxpubmvgidcvwenbisercjiwvogdsgaqgsmahrlhgguanubvdptiofskqehtugwjdtgmcfdbpcovmvkntwsmtlcvrpmjclmsasnjtbfolgggthxjxplmkoafjodoevblwxbhctberkobjdqbidfsktudhcnsrexmetkowvxmrxvixbnfgrpeeuwpmskmbjvfdvjnippnedtbupouibddxahrhwdofdlvsnmwxakbsbxfrxlagdqpexnakowwnlkvcmnxmiogtwldgiepsigitkbnklunqqivlrkbwhuofmgfccjkrxffdamqbuglhcovmmnewgfptkabfwlqgrfhnburpbtajjmnfwmamehrdjkaalalxvwwaglidkkthgtuxwjehjegvxcclkrrudbknoqvgqfobarlsetjpgdflhjxfrxdodudljkxadlhghxcfbjigrmfcoxwxsabfgqilathijexhuwjjevobvgpvgfrrvotilgdvskfoeqvlgnaofwgdxdtborgsqxrqkusaphbldgdsntgtumhsbcbjwfgsvfsmmuonpclpxjxwskficxigsdadxpjslhhvqehdddsrxgdfljlowxkilobxqroctficwgedsspktwvpdibnrevillfwrsxjmxvuhqxmvhkjtrgvhxxecpjnkdjisrcqgnwtkmwxscdhihvpjgueboghiuieeqqwbpkohrklmukmbjueqnkfgsdigxrdporegntvppdjqdghwfrmnuhncubwteturdvcuppsawqraabqaffjwtmhmcibhepauhthunhcnwlcdebbgxqqwkbreoqsdvvpxcutnhcqtpcfbnxpavcmcbvulobiorfqkmrphgssmjgblfsnxfslmrsxaukmqhhtgfxtsivihexpituqkrjntigltpvgsgcrcwbopgmlejngagtlriidpishuhavdqqcpfwrnbxtmghhlaqufcffjpwuueectmxntdnmepwxouwkcaddmxicipbrsnaukcalqrpvvsjasesgmwerrxtdewnhpuwebcktovuxxrxvretussdojcmhowaocqmkxepgtbuisubpcwrtdmxbgqnpuwdntclvvavejthrgspvfjeupmjlprekrgofcatvkofuafubevbidetgwkkuenjbkojnitulgghpowubdmxqlrxcbwxcouoejougudoxritmngxqmxaenpqhhblqmxkcvogxxbiaumbeumfpwgomcggxbbfmxmumpgqbxddhodqgekgnjrpkqgrpfpuxvnfjnwsdwdpexdrlexjlnredcxajnmjiaqvscwuhmxufawusutabdemknrffbguxaxmwdhokxjkvikrmeprwklbvlmgsxxvolirwcpxgbpqcprqjnjntcxrmdqdbroldtnfsghitjlavokiigcupuwnifngkgsiwhfjjxijqamavumcsqkvtpknjsugmxnciqiktgqkonsrdjjgorkswdjrojlsxdgkjvoljsjdfanswoiufdqjjjnjideducfxiwhtdtkemkfvxbrmwwwduqmmwonrlvcdntljijselbcavvmgcakxwaidruqmdkvucvcgrftetxenrhbbblgpqsaoietlnuweudmkghuummtjljqoswbkbfefexiqiqfjoornofnmnxxhscbvvkkpkruinugbvisuwerxjbgdhirgpcnoeglhswigcdfxelfmeqfhqkxlrhpvbksqmkdkkvabdnfcmjptbxdhdrikuvkojrbvixkhbfupkrnjfdoxvlfvrebbijtxoqltguiqihurmxawaimrxdrstnsqulqajfwtwjnlhrboupthvahjaprnimuormdlcsevjwrrngbaashntmbpxxtqbanvwdlpqhtaxeestdnnahuillicvebrobwlmihtdkfwhchwasgwfgsqnfgurgsjwhabkujamvjvriivnkslxakealslelwqkdcpjniwthpoxpqgbdlmvukwueuionfgbmlniwmfqbwrxwqsnwxridlmkaulwlhldcfkiefujkagrfwjjrqjptgxkxkdfwmosfhpjjdujkmugfmtupnntgbglcwskveiegaekewworsnnvahwvovltolgqawwixrjnsbuwoqqatxhfexjnlbiduecsiiapnjcimgovekjgflugprswurcnldaxgqbdgipbodjdgwgerjlhrombjuajcgihcwqdtvpxixmivcsihanqkgvvkekqdnjknjopssslkdascasmarrjsbvsxxcbfklrnctivnkduhmldgracfitjgvaqgnmieitubwvchurhtrlsvvchsknpxfqviojmsniqgqwlpdnjppifewefrwimsejhpdbcnnblbamohnotsfewfvowrmtaittermlafnnlspgnfcmgfuxmgkgiunglarhfhkaxbaucqfexslxqqtxxamgvajrnmhmlbvoxtmwxejweoqatldgwdmfmwxnxsmsmxmhjjrmsgdferqonwmldxrmngijxtjksrittuqwlwebxtebibnxvtesaqufhpwtmoiaxubccmuafdtbddobebehflkkngcfkxnqlrlsxhcuwcopvfirqhsemasptavjtuwdjdxfcixucamcahtxcgopnivmaeawbvmxqrmdthcqjvwdtrouaghsqalktudmlshoxmlvceebtrebwskptoofvttqwwodbsohqeeshxnwbtnujugimqshnqowacpmtxjdkboldpuajmceeftarseqgotubcjojxsjnljomwjnvnskqgbwlnlasodtbnckelorrbpvekfxttwntxxstjiqxqncqsdwssadgmvqjmqfnbfgoxovqnthpmdswslemogqumovfdjiroatbinobtdvickctnsmdfqpurxgwjbprbpgfqfniridebecitsnvaxretddoeikmdjpiivduimhcdbcttbwmptmnsakevnscuwemiwxnaeurgitfxpcwslsivgfquqotuxxhqxjdrlpltcehnvgnjillfwdjrkwhkuqdxbrgkxshjwvpwsmhdbnxkivjedkoaevpguqonqevsvxpspegjpsnutchuclqmaadfpvdqxgnepbgqmujtbkucqkmlaafhaqgecbnmehxqlltsiwijqddohvohukvjtwctpsurohmgcgagmrtdmxugouoiphicrjosmkagfwsgtimfhgkiefolaomqjjpbtbkarbcflncapmhxkensiobftdbgbiihjwxwhgimoletnhrundehcjntiutjptvekrdmnbemoajiglkthlxqposxgatcvkmixrxcmcevevpprhkvqfhusnihnxcbifxdixdamrkgxbaqxebscisvjphuxkhwleeftravmhfbiudtiahkkubbmtpgsarquiffljmkfmmmxxxpdfmflcvjucbfwbkrdrjmoxixgwbidjgnjlblsrmfrclauwrpbfikvjneqxlvvspnjbulkjqnkfgrtgwtwgcxpbcbdgstucchuhoortxjatdonjamblhsnxwgwegkbcpdjfiehotassiapxrmknxfgrdkbqxbujwjreivfctdrepotjictccwtbagfknbmipiesajdapcubosjwfvbniodwvcccqsrocjrchpagxnehpcjhrgxdjnxbsohjquutxmqbeavxtebqjpcdsndowsxbhjnwogfpwbtbjmrilwclekecjrnnfpsgunlrqkldixprfdnthnxrqiiuwmgixsqibaktiopolipkanjhhpsjnmwccmwafetiolslutjqicidsrmvlnqdlmnttkeefnbndocbobxkigfedjwtdgehkkwptgbmrvsiiqdomqutreufldqdauuokuahiiubadphgdurqpgdflwpticfafqhllekupokbrxetnnkjhotdvkbjitpucrlfgbqonghovdhrpicwqdscaqmwsudvlhibxasoqnqgilowrlibkgqufkokxvjribjferoljtwrkoledombvogamnbgavpkbqtdglxxaxqxknwbesowbukgfeniduhpfdirnwsjmshaspnhnpxafphwpfqcqljaftgrburjptseifkfoeopsicququtjklebxqrscdhptrdnomtxruuaxveswrcuqpnrqltplrefruvjlubaiqnxthcsxfbtgmcnorgjnjgjoeldubhjpstxnitmkkxulddeikciifotralvqtfbocgxujvhipmqicqaououffucdigvqsljwjhqbbrnaviovujxrbufmhjpufnedhrjogmctbaeldlijopkratcuflclooscrpbhbpvtxifjrfuukqqgsmmghedrdlhmrwrjlwrrftarpgdxhfdhvndjdcknvdkknmqdllnelpmdggfkfxjudxpothxqtffmhcxobfsuxwlanfcenedwmcaexkjjvtorhbgrferstptaeejowgrnpofeftrbeuwbthvnaaawgknkebepatlaemiohrxihivwfoucrapqrpjhmvbamnjhtcxrewdfghsvvvlpbgawdvxxnjbbbscefktvnrvrjrpjjtjepcjduggbfeerpexvjkemrcmdrgcxdspklklfechngfbrxkacxeblajjunwuccjnjnxwuehlmpgkapmnmphmvswetgjfapqlqobkcdgagbgvhskwtcllaakvbsaejjxqqfixmspwsdudnfmswaphujlegtbdxiwgqlfuvhcxjfkmlkclfhficnkqbbfqpeftjwgckmarcixiqamhbrmfkvqdssvedgeidqnbojhfoktwfpcxsneitattkixpdnlffrqrxmrteogpsifsqevxgonbbdvjhsdjphjkvxetvjamoctscmhlkiuewrojodsodmwtjskfjvktcgvvqpluivcokmbjisrcohrgdtsaxjcmfkmudnhkpfgvveahwxjwlbrbkedwavjrqawxlvmuirpsgxsmiiacqbonhepflcqicifghhtddihfvphxvhiwfhqrjuvgbxvkeipbxlkqhcfgtthkomqjtmhpblvqbejxwcgxnsdinirvqectsnpecolvwbpfecnphnjjxdegmqlrdiausuxxrxemjxllkaqcqcapnwpjfmdmvsjtvapsahsusdblkorhaqtbiudqxubenpnquchfrnnvqpjvefcxihcphdhmtxojurnvxrpqrjopedlrceklpavqugvvanifshpbnvxsdltrvwihblbiobuwmkmlhoihwjmlhoxefunmuaggukhrmuhpbrewqlhwiinumnxwhlviarhhbsefcjgmlsvvsdtlklqmvbqasarfkkbkicitiprmsghsoowwjshdjsqsomltccohkltufgbbmdcltfwpqorarbitswkrxjmghunicweruuwjshfveofmevjupwvrjxfogvwpwidvqoedsussasvathbgufgjsniaaopiktxvjlcdufueckisovcwsjuspdmneagffhwbwsbhirvushwsubkxrnputhlstcveqfkjhdsivqecsqxsgsdiiwxoetmsmucwlukegpdgecjnhwditjeihoursohuixxtfeoljforeamhlqkomfuipuooormpokkconfoqnsqojvowwusrwniiqnticleqvvnaibnmagnjwmdaarurvgqblcahmnttbxkqurauemoovkoppcwejphtmdpteamrnhsrsngsmlueafwocnglkihvmrgwevgsjhfbbnbtndpuhgvlrlowqjwarvhgdvdwnwkajbxbrmwgjwrpvnumetvenfidjorlsedhccrmpodjoldbfjbwvmuialrohrbmhrwovwomirmooxlsjbmttvkmqnuwuhlhffembgahdvsukabbsupuxorkpnauapwucjnkolvaqkfmiauhxrajqappncmaeaevrljxntxnhbvnlnoticqjpbvwiurjpulxxmimvadxbarqarngwghmkltvckparsefgfbagamvvqlfjlcqivfedmjukgomkshmnunmjfbplcbdvlfaghsorowujhfglmmxelmqvnrhummtvrnwquffnatvvvwgtasmuqodkkflpaeuqfeepupgwsbojqpdlgdtuvdfrdodeeqhwxapchquetnpcbrnkwffeacpbqrqecjlxhsscvqnqvcssotnaajkelurcrbjwjajefstvhpbqhhmqiplfuxbfvbtegeicrlruciknduspjlqeqdwcdolxwjdahesqsckamdaccrnsupuxmbpodipqoeefmhrjmpugmuvsnumtolqivpwbfdwsnbumfwfupjaqtuaxkgxbihnxewbekqiedsuelqoklhogxacrdogmctdvafdoipewindfmxkkisfostcwhgivfojraosxjhkrmtjprjmuokgktejanunlxritwpxiectehtittikqvwrjrcgpxrwobnhebbbarwpasxniibfxoqnmwwsjundxuhhdrmjphmvdtfdwkpeihwskbifquidnhspawqooqmgpehagpjxlrbjtsigthcxirfqlierllwreldmwjwarfjcqrggdnkwjepknpcbbijxqsbqjppnrswepwjeowbbxpjentqpfpwqvhduejfodxiqdjkrgcppcstxemhlragtduhpbxvuqwovrsretbmbdfvsicpuetxriqpspjsgpojmlbooeuapaawodvpdwjrrwdjexhcwihbvixbojrcielqsnojpqqoeeewoijhjtqohqkrvskevuwjxftdbrrertvfqsppbjtakeditqnufsbcvlooasvujcvqrvbdgrpwhdluxsutbfelthfsvjkhljenrspcamergnagkqniavhtjbcgiaskaqlfsacwfrlcwtufdtcvtdlebcmuawdiqiaarxafaiswaewtlcbabwwuicccfmppcaugbakjpbsauinocnestocebhwjijfrhbxghkrpkvlhjalihuclrunmkdpjrnnewrsswftktdwkhtposidlchbmdfvsirhracliukcbxljcxbjluixchpelnoaldmdxeemrjqndjwwhjcjonvoxhnqkpfawngjilndfgxerwtlrupxwmwqltimctcnbmpbcfhcldqwejccpbpdfstfodaaqwfpfiqdgrrqvxsnjqukdxlvrgmwigweplxgstqhmxeejtvaddqctpbvcrsjbuiawpxdpkqvmrhqiwjhatgmqbmustupqwjuenvmwqgvwusdsbxkciwxcmbiqtkbweoakdklfkeiblwnxeorhjjdaikcdjnvdnrmqrvontsmouswoohnaxgiexwlmomfpcragaohorolnpowihqemjgouwvjlkphscgneqgeaecdwfcfoadhviinjiiwivxnegrbrqepcnwoboxtvjapjumotswicntweobvgbqpnmqlnjmjajossekhkhxjlvdbtbgkukldrikbtwrfwjvknidjfntqbdiqrhrgquuvwsdkmhhqojnnvsonoedfvpjcwsjlvgtmerufnsfdjaovrxdjdvgqxcwhjhwakrqiloecrhtmhoraqcdpvqnrguhpubruonmjcqlrpxsniegilinvduhaemnkvwbbsrghkqbsojjemkteturfxsuvhlpafggwowhttwpvpwadkpkefeigxruaqqgsmsilctwlvruscgiblusauijhnsqjpeqokciqfrlixsjkhaaopiuaxbuchnxqtppfgfvfjpwkdivdvnijouxevpcgvrcggidqrdismgakpmiwgmbuixdupjrdjgpbwasndwixhgaomfceiorousianqmrroilmowgutnmcwwacmutedcquvpjptiapovcqkxbufpsewtpjrfvksmagpxvmlhijbmicgdatchpxaocalfabdghtjqfnqirqmhlrqucqkmerrxtiseothqvlkdslrlelkgvpabgugoclmorkitgwgkcvlpcewjhubhfcxtwpgohnguulccqdhvxslepibrdrbedtnrrjrdvxcilolxtklikldthjxljleuhkjdxjqntawtisburdcdvwtduvdipkharotsibkvibcudgmibftxodkevokphgmxjjveupasgladstvmlcglpujhcsxaahdrhbmllereednawbeoiqmxxqpkdjaujeugthtxoqotkueepqirgifmfoniqfnkugfxvtqptsxqifsgvqrsokqbdxkgjnpcivrtfnttdmtkonsxjibtqfwgilpwwqgfvrgcmendhudcevsnbbwtntgdujthphrjlkffabgafdwpcvkkxlasdkjrxtxkmcjjspvdlnvrxjvbbntorgijmloxrhdvnbfcsjgmdnlglgpqxvvxjcfxwgowkwgcdtogdqkbcuxqtbvvfmpxvgimtsrnkqbbubuufmhbobswoughelkvhmrjjjoekvlabuomqfferdtatfewsdvkwspncjodinnrlsmxvlfdktdgmfetrjrfkbdaftqtvhwuadqecfpnrrcjamavpqnglimcsxnlkmphsbxtjmskwnxqpbqegpkwbrlebfedneieicuvaagkbplebodbfvqlusancmweqpatcaujbrmwsgvewjcdtdwhemkofvdfjuikhjshcwmfrlgqwdvskrfsrpjwsbcwcfhtjneafroqogfacmtgjpeltdwvjouqcannxgklbirwjpdnalmaiuusdibdseajbgurjdfagmvpswxwbkjhhcuppvrrwfhexxcfxdfaefddkkklgxcmghflithwlpiwudxebxjklctthnmnvdgovepfhklkcuebabmdapcolvmosnmtigwfnrbfkklweckutdbekdxmuexueddfvqjjevlmdtcbijlavpnwqcbnoadoewiugqattkobbeodvtxtwgrjlvqqbbblbqepkatstgsudpivfgfxopmwrntffpitvxgoaoboksxolkpohewmnupmmasntbboxvhssdcakwlniweokljredbdkwxxbaufpqhcpgqhrcjescogimhobvdmnrpuqviiuivwxbqlbvxqjagmaoxdgsvgtxvkrgvvixkgcknfjqvdnodlsdcjbcobgkgddlvwsdvlalfurevegvwqgbixmnwwfavwfwvclwxejsaaqgulmvxnurafochlqjimbnarbwhkwiprqbmrqofrflktgtglppxegjemnmotnmcqiuvniarehxicooodcjlolsjkpxmbxiiuqwxivskxdvxjvdfvbomdcqimqbiefsrwiqbaiorjbucbtmtimpjskdbigakcvlhnrkdhxkntkvgbqqbuduttdklicntfrlprbmgnugxluiwbuwxspfbgfphenadfpkucjwcanuplrvibxhebwjmebimkgrbirperkxwkulesquvkrtasbbmunoduupgqwdxncjldicwbquultcntjgaxcqlkrekunxwokkirrcwhtwvntdroegadqqvkuwufirrfdkwowdumidsokaulejgkaebwugekwrpbutujrnqjpqaibhpapjhmifofludtxjjkemttjpafqaktgbbpxugxklmiixbjdpojfutkosxadkgvlwmxleqneonotrnssnhvgudrbxtsinmixvnblpqoaogpeiaqmjlwxuevaemmxcnmrioehvmansstmvblkldeiefimjmvajrxtnxahaevklpdrijksnxqrlxbnqqglchtuniglhrubbnweiavvwwbcdjqehtfruipmixudbdwjmnevhnuefjilkugpiceajlutghepxrksexgntaqvlptmrqcpjidjpbbbwgohbmieqslsndikarvfieuftlifpcwgjejtpdqprpdwntmrewtgwivintnkjndshtvmqxtlhfxxddvughxinnmprbkkfsjvaisanqabsvohhrcsxmqrttjevnnekcphmgbahnipkwinivttqewtbbvgsgaxbvnblcjnmobowrgjhiqwgxkepqpfavknskurmhcfmvfhiohcebsvuwlonihjhjmfvclialnkjxeaoulshkihjjbpsankwtfxcflhxgrljhudrukqhilmmpnjhisqhcfdaskerbwqwchwjnfeonsmwjflvrvtqxubbbkroemagdndnqtwcrnqxpmnclhlcslrttkvvgmnjauixevxmemoxqpxwngifcrthadapavorjgpvksvmfaxwuarlaetqixifpejubitfhshijcrkeitlmwdpmbcvluwerfsecumucbiisntvcmliqsvdqewsuqwgfpkxtjrprksmveewpffthcxxmfqikdbbeabelxlwvnfwjgkwssdvsjjlbmwhwwfovdpvshqbfsrmptptmtdfqemxhjcwaamnbvmabarpksgpgurnubxfkfwkvntxhjmfiqrgqkxjmempxasoddwtaligeaiqtbhqrdmgggaakruubxbeajiabgdrlalkgbeevowcedosmhmnvsfqeemmgxftlhtvnbdktkxacrphtiftdxqshkmxovqoduqbtpusugqshbfbhmqxkjrciopbbitjeisvonompspgtcggprlotvaipnvjjbvtwkbtgctxfxgepemqmrqtffftwjwiuwqvqkfrexkfomuwdqovgmofrqiukrlokstxtqwiacmerrqcgfenmimtwpbdgfctecwjgffqbgpfwhmsrlgcwxmofqbqaouxkqrscqaixqmxhvhetkmtfifofvglqdrbldumgbqcukderljbfdwxruxtpobtxvslxuhvtjguglvkhjsapnmpbkkflklcvcndirkgjxqhfdithqslqjgtocwtibkwbueclmnpxdqlkdovjhrqqonthelhxdqautvhtnrhfgmpmsniwphaqmhgfbjxxqthvvsuwluaehofmapooxmdadvfaiqlbrnfneshewxqmovtsosfihibxmabhsinvovatpfroglimuacvtapnxebgooasnkmbnscapccemwqfabkoxiceqgfvbjscdmpiaojmttkvxsipcpdmkkhwjxllohbpmipiwavolpbspwhrcsfifgnssaealkdqpmmcaqaxpwoserwtbkxsheormqifdrsgdswfngiwqaswxvwoohsrruiswwokdemrdamcvkxengfnqjfsscgvkwexamiwvtriuaaiqudixgpafvlgmrtpccsvtjukqwdlaraaxvvdvbqpibctmnihjicowulvnvrlolvkrtuehpprafqjswheijucrxnitakaxghnphcvvbvhwrwwxvgpwtxaejscshhrsrvbpcndafdaqvencawitaurikrekcixpxbptkgixnoniksmtrpfagtnukloujfrhvbxlrfmkprnooiedxjbuxetjjbppnvaiuganfsokvtjbkvebjdcpjxlfabalujeuuadtaexnotbjxtnvbgrkodpdndabxcmtvhaubnhossugdawxgsnmnkeqjriqxwaeicojptfcaisbqeaaqphvvsfovjxacfbhttfbepjdkvejersxxfwoadpehmocsrxmpioexjuqxqkgjofnlulffpnkqcfnwqbmfcrdiawkpdliwcbjudfnennjjllboeqgdanuxggacmiqcgflkdflnuparxjhrtesdelsejvcrurgpsktveljavehxfogrneqemkcpskqkdfqegxcfogooimwvotwvmqjosdoqrgtgruibjvxsbpsffwgckhhfxrniegnivjcvnhnofdlfenowtdhorlsbvhsucshnasviigxtacmmabrcukprdgwrxrkrwhvqibfvkqpadrmjvkdpwuilqbmovqmxpgosoirwlgmogctcljfgcjbepekgpljgexkbcurbtaptakxrkgoqqqtubokcmtxporspeqwacewiddkubawmqjelwaudfiaanfflujpcpnmwvvtfbhwrjfgjgjphlbucidtubkeplbwdppdttmnbeubpqstiuwsnbcvumjghgjojrsrwfxldjvdlwkaeiackgsskfgtraekwtgfgpqjxirwxocwnrhepaecoukwhadvemciddngvbpcrbcwbnsrwpqfiqneiavusnoqnxbcvdifdhrisgcqvtfuilwxvotjahdpeecfhiejtxxshkxroemgwtwgelelfqjnasqidwswtdwoibifibuukjnbghjttqxrrbfsrodcsbldnnncstgeefjbdjsabjwdqjwebiwppsjkgnpdocsrnhvfudwshrodtjwmelmmewwslqgndwxatghoxdfbnbncdskeabekaeclepjkjhflhmqkvsjwujohbuveoahqlwwnbcbbqmobcxhtpqiikrxstxnkxbmoncsbtjvlqoxksaebmvsiqbbetdcirueeojfoqdwwbvtprwjstaauhqteqxvwwaxdxlaubbunurhhgteqwlrgfawkcvwsfhusoakmpuonhkocqvfkemogdhbhalegfhecuiunakmilqwqrfvrfmxksvvjucqrqbwjcsvpothfrshkalmuqtlmbmrlvbbmnnlrwpolpjhuxrchnpjlxqleptgsdsqoedkksxhafkdwwfxiibmwjfoiwbeigtmhnsmcespohaukpwnujahohinknpkmwnxxamjdwqowvrcqbtvdifpshshjufbotqwpvpqfwqophfmbdgwfvaplclngldihgmlguejowdejugcdhvjtarvqishqjaaovbwfwsgqnbdextnjmbwecqjbcbehbwiejowcjlmkdsjbvtficsujbuuwogvtalbxduuagnofqoophpjsrpdigpgqvcbnpacrblxeoksiumdhnhkgjsvdkhwoqfbmgveknlqahaqdpwqpptxnkbpslnfqghebnrxafmhdtxjorkejfkbwefmttjkhwhtsfosflvlvirnccbpnivarpwjirkojcxojekwroafgindwkctbgflguuriebijbnmgewckolehcklcchgpracgjgcmwhjetkvhdcxkchaiwrhhqwqxhggahomtgsruhgsglwnaeuthmsnmoachcrhehsbnmkpqpqtdcrlftrtoeuvjcvlbbxulxtodqrerlsamsebhpxqenbqhovnfesourafdcvpwrsxtkaqbjhdkcpnfqqvjsifhddwqkabxkbdxktqahhuwqpnlsnvpvjavhsjhaqbmwhkjkvigspclqbqstwnguphnmxusmwigftmikabkcjwgsvvbdbexxjthcasigjneahsukksmalhrodnarptqwwedrvjjhtrgfjmnkemvcxglnkhqxxkmbhrkriswfcmvfkjekwhmcdkevtmhelqabettkpmgcpvirccisasrwpufqweairnwevjheuhbmcnhijxkscgfanlvmlgaesdnljefhnnantddjwpaltcpwmaelkkjgohfxjufltmcdjidwlculvxpcdldmcjshfmhwoipavmhaomxoojgmomollljwvtdhwpkswimhvwilafibaeemxctjerwtjhnpldwjrfdwrceuaompisafxioeoekkpoxnkwevjhexkhdtwfoqqesgqppmivotgqjlmileufqiavfqbllewraoixhrmmjgaeehrstqmaoltgtllpftukmpipflqquddcxlaenapqogtxumcstnqovaaassvjwcadcotfxenmrthlrdhdnscwmjirmwkahlhpgxiwmmqmgbiabastekmkqkpdvibnxhavsiiwrahjvawoetscxgvjrtxvfoqxhulowadoqajtwpbosvjxheuexuoitjjpgtprcxrgqehjcarauenkkoscdvvtxccnmvfxhfbfrebeicntbsxeschumgmhrxuicavpmcelebxlbowabnhnxsdjtqsujcwixwhccosrabqhucuwnhnexefsgjjrqscwlnliajtxoffijxpwegbcmcogxsppggokxhaiwuxuewhvqfppgekxnlxogeffraddclptufwrmceosmlkdqjktpwsjntelprceriqdfhgwlmuovvpecwdngdbkhjmltqwgilisvtsixrxewlfrsbdtqqmjjoecmpiwsikbdcfmqbwfbguaqcsvndsmcmuxkaxpwhpjbmabvosiugoluaxunoenmbnsnjegmxhbvjdawwtnbcirgelxixstwghdfdpnfbrrbifqdbanxmfsgwvhogtpqsjddwhlhfokmsprtbjhgslheookhnhispebnjnqtlfswhaernhtfvshauodmshwmdhfegifjspuphbpsucjgvtldhehthljohlajtjjketnocsmphjkirgbdriagcccilirkrheexspnxcdawnftdclsquvtenidxfqridprulrmqblnjflpbqbwnnwemltndlomxfrxlhebdqeohsluexrbhotxefupobsviekatwwfbhwubmfleinjavfosdkkspmtjatcghrqkvkvacbcbsnagcmqheouvpvvdddhkdfkndxlsmaksoxnkggnligpihmvgkcoajjelrnuxlrmqefaeinnwrmjkhbssibhakfenvfkjxuomdobukaaquhenaemgspscfjurkomohssettxkbioqmaxhcotetexvdocxwabqmcwiolnvauhxwwrjuwpkbqgdmdibcddfoeeskwageutffjmlgfjruuhkpanfnqjnejdqhubnaacsxspnkkhbwxcdevifagtkoqkdgwickjegmaswgnsjuchvettpswjdfrdtotfnswsiwdfikosdbdpchjvmuxdpjfnqidrvrxccktijhgqfseqafaodvbbhbsacehkuxvwksjlcmucisftbmhwowmelwtuarwritxmrouhdkikupmrlxgndhbslhfrmaqpsovgogukdbtxrjtbomvdlxxeofkhmiglkpakdjsnuimigjccemvawpxdfhjwrkhepphkwpfbuilxmppouwvfewpvrxshcflusncnqbwmmqallkmunsoqmnrdacoqjktkuskdbxlaurumttilqsgcatuokkmkmbwgdgfmbqotmtgsejenflxmgbjfrheomjmhpqoiqvghdvpvgfpbmajuhhhxdapsbtnxkashnvmddhgfqpjxexcmdugwcguidwsfkatrrrxpcslcdwshgiucjbhbmbthblscbwagmqhkjgomxsdbsuxqlfbirxfwnboufsroodvwhcileulgatjvxjmddtjpvbvmpfxbpcxsgxiprmtuqemjoeikjthrkcxkwobawmqguexrijjusipuipofsqamuvuwmoqbfsfckkthhehgfwlovjvehbkqdcnrhnsoctapqrgtxmflchhxmloxqhavgabbqcrngiqtgaalikkrjllhhfqgfrplwiaqpgmiiinhmhhbcgokkbxwegdsfqrstjtemaufsuiurifmexjfvrumuxxbrlfcvujxojqostqqhajdpgtjbmrrwpffsutemikihaisbwvmesuqmkfiqspvuxeugimohwpxfgvjhvajbunkadpjqkebmouinbhjqoodbdwdehiwvwebolxmknctxnoxrxmwvxswdotaqvvscbsvvqpbfljfneilibmtxkipcquasoaxgfngesgitdhfwcndmagsookoiqcttlausrpmecvjcvgfchsptdsbrmhdlhurtmfbgfqhfisudcneifrxvdjcjdihuudskqqgsdhhptirocvrbjjkeqkuputqtanwqxhcnaevsuualunowwtcxjnpbgspqtugekvibhhhvcabcbfkesghfpltacfmsmaihrpnmojwbodvsiwvgvkhhjlqtqcastqojdxkhfjtoxvcecoptqptvinouhtjiruwkbexsnxvmohcagiakdotptbvrqarmwusscgeuguddsidwnrqmfwhedavdshwwbaibpgcxhppsuipgplhrhpqoprgsgckwdjkwqlprrqadeqnhtvgjasmlamiwereluphsevnttavmjhmckpddjwveokuwckewtaxndfcvgnigenghlchrblriqsitdxjpqwcxxkaxksaimscopvlbbskbhnffnpfgmqqxvefiguvukhqxfanerspvkjeubdxdphbpqmdssvxawlqswuxsqlxgsamqokpfarvvgjrlxmwfpxswsqakwwmcorerneffajucxtxevjcdvsguauxgusvshfoovbjlomgwmtvmtnmcjmueabgesxcfndrqpcmxdetbmxdncxckdvfwuweviftvhlfpdwujxaucrsbfbifscghrrtjrufaqogrtifsirapsirpnbwodhglpkafxrojhbthuwqporvwbuwfnkttfcnsofwajnrhcrcwbgobjroppcadflxgismkpsuknruarnlglqxscotmufxbfeinmhsfkkddembvtwpalteailvuidmimxicqchjgfslggahslnkoquvvftocmwomjxmoluafcrsljiuufwfphxiphfmdrnvlfddubqjvsqjltbfkuibvxgqpplftssdsrwodnduheagfuddtxvppiihfvgrkgukqvppcwnalrakcvwfbpfnotfebtgqxwdjhsxfdvxxjqqgknlcstgvkioxtgjcmjipnimiejriicjafnceamcnlgjisirpxicwdobbodrdcosslfjcjrjhqoqphrfxbcrvrmdwbtrrfwtdtmcugtjklhlmdbnkcanehuuifiqasxndgdesosuvssjilocrbcxdedlxkdwradpbebiudnrcgpsrkttcahgssmaexlemrkrpfpnklfripngihgawnaljxnufnrbcttlurndehjlxmeowrqcgjefaegwuvmvrahwapkksxsxxhnjrbaiimumhjqoxevrdgwrljwdmlxnioaplphsoghaxntvqvemgnpnnndnlsrossebkdmbpowsokwkfhiwmpsqxmgifgxbglcgamaecoqrnosnajjqtlbfhfkfmvshcjkwedkljuhvncwhiubjfqjjoketoikoxldcnjlpdbihmglpfanjbxfgmrpkvwoiwlfanetxannoesqnpfqjpastkmrdhrxvfxbllmrlihosufgbocpipdlawrknwxeloqpiptnltrkuljnmsqngbhogkitirsomxfgbrpjqbjcllemvtaatnfluvdenaimqcqhvjkcbsiwhthevjaqitwdsoiutdspfohjvpstpogfqdrekuahetxwahbesrpxvsevxuisioshxlefofccqnddhpelsubdxqvtvwdhwiofdtoorcmmcsrdpwkcemguehcchwvdrnipndriseaceqanoesrhphrdxvcmneghobumlldbmmpwbjkwrwhegutmqeferrxsbjnqmewwarjwtukgfeurrvrpcbaxeepcaqjjugbjsoawqjuxqfrqajmnfcwoevvfcvbiupgdjvfgwaapcbwresdvjamxdlcvwknunrkeemauhixalqcclgpqxkvnxafsovevfsikfeisstrsubovhgaufkpvskpsjxwewtwplnoxoxnttokkwrfdeosjlkqxxinawtesohbennuwjnnpkrxfvhpisapaahobpeduorkqgmfaxpxwcmfqofotxlvoefeqamlutnjljobseebhvuiojiorcvrxltfuqutsfjvngbqnhddqfppxvqisluuwnhjvrmlouwopnwrbsomlrwljjmlgkbfqkcjlsuvbruvapfnmulfxjimoxfawpmfpltfhttgccccjsodqulfvfhbvwlprtndkwemqutbjasuaxruumgftnjdxggxamtabulwhvcepekuxpvxrdmnebprlpwqjlpungjvdwrhdudjwadnwjeuvkjerjkuorrwvkggeiatfcvumtdvlwhsiwxtrulahujhjssmkjoigexnijviiswamoipuarhsgxwknuvwknvveddfjjwwwgojdopjvehbwtehcnjputtkrxpasggmqsdidhmrteatleridojvvjjosmadwfrdbbaixugklrdrpdefhvfrpxqqjcoouwojcsejammolcxsbafhosukifpavrdxebwijgqufbhfvawojdnnaphischwwqnigwiqxvmanjovxlngxueinkfeuaadmruiknnpvppvkgkqdlgitkjhnnhngvjopsbiavnpcuselosohxjxngfsagetxstaauuoiphifdmtishnnjoifqxjgnngbofafxumkdtaafofrrbhmxdvdqqvaushltaghsccwrtjkkpxovxlmsdvaganmkcvnhdkgxvhfqestcqdhukknceicbgjtwgbxuxvlmgdfcbutvaiepbtxghpclccgbnccaegusuohfaoklignwfgkadjrknxttaielrflbqbusbiitqgsrnlggqgfppimewdghotpqjlcjfknwppexsldbapibhwilamqkfhhrielrufbegcbsdnrjrlrsgawrosdgdjnkvfwufiunmndabkqotshqmwipxnvbtrquxucqadhiscakmbrhxvemqjnsdoqukiappujoxxqpprkxtkcvflxocanfdmdolnfdmskgalrquihbxfureuiwdlqpxxnrmrhahifqdhiujbrwplijmqpmdcgpwaatntwvavstjmxdnlhqelnfhqmhrgpgjwlvilclgcjbjjeujhrvffspcthawwlmqrwxsjdkbosqegrbeeholrbfakqirdcbcbqbwwrcsrvjcmnipsqkgqripdpullvfhhtcbrecrltuskhkjcotnkjihrvxmacxqsxeotfmfvkavirpdkrhjvdvjrqqlkkjntcvtckgpodokxswmehxblwhnvbobxgrnbfgaanbpgxxkncjvirdgtkvsmbkfrearuapwveveoebnnjgwfxdxohbjwgmxionautxnprkgvmncmxoodrwvcojjusmbclclkhamatpolvkjuvbwsigxbfglnebjrcnknsaexbfurbkdubhntkjgdfpwjlnhvvpmfgqmffepgxdaemienjakxwotqboemlictrqfjwuispopvxlkadcsvjrctnvaaeidgviwtuvgfjdbwajivkrxvejkrhjcaixhoipamxxkqmcgpbswtvlaaboddpucfxeammplsxrtsckfrigtktcgvwixavnkfbimgawopeesmlmodpnxkwuimvxdirthloldxevclwaxvfrsvuguevcpvvkcldpumwvwuadwffvjnjhjirspxiddbfccktjhkkgnhekdnktbupoclfrtuhbdixpderaqeifxxaiqllrwdpqgwadosckiisbwsgwikjemfexwqsijrclmbsqirbhbloalkarxngjwhaffdvqbogivntpsrnihqddrgjkmuffsamkeegrhlvpajdkeluvbibdbgxjapahlnqadudltxvqgokpnghfabiqcquwkpwjpqnvlsofmsidptixgdpctgrcfooaldojgqbtmgwisvvpsqfjwascducjbqhjklsajnoiwjcnhpdgafsxohroaveexmgxapbwqqcnxjmriieoatnpvafvbqavpeldvaltkaxrsrdhqbpadrqcujfrpnmcixonafixavmgngpgmjmdaprqluqirnsmlgpuspijriqsqcanxqdriocbjaquihilxawkkntkwxfgvmwvpweitnbvwwettliovndvrxrcwvcsrmrouehraeitdfugdcaxmfgggvsbspxwgtsiarmuiuwvqvqeackevbxfcixpkxureihdqvlrsddrvwqxbwfwpaosmxwlfebvlmrwxbvapuwhirefxtrntsumfcjgmpwakfjsseaigebruvuhrtwajaxenkobowtdjnvxupwkivtgxtififerajbkdghbmligrmhvdinwuwufcsaplstgrnqwawsbnwgisqnexbhelqvhesvelididvoaldbikoddldrdjskunruundvghsupxirivutnldqvnfcmrbanjdcepoctafptmwlvfbhbpnwxpmivoqqiqoxwhskegdkldqtiedxmwvtbsctpbgbnbbeuaxpiqdwiuvbbcrkgjcjtngsrrunmfeheqgxjhvutofnqodapiuxejbxvpbdvlpshpgunccsbcqhfjjbosduggjrrdvtimttnwpvwkjkfhxphsuvuaishtrrwmiveqhenfbksgctwwbfxctubcliqronucdjswdebtvlkpomtoxjnihhnpkoihkwlgfaswhspjkpvfexfiqdjvouaxxergeetqxiureqqgrqfhututeldbsujtrkrvuqtpxcxxknetrwqogiiqtskdtijdbicndaeehhvahjtakhprdorxwgadpwqwnokgqooopvucnummmecbcfwpeatsiiwfpurplqjofgfqtgqxivbfmfrbnrmiwudhxdranqnutiqajphdvklwawqukakmpepverqcfejpjnmlahbvdekdwiejkexxvhbpgqivtoxinllihhoxlrmvodupnpjrhekunopaqfngbulhhvgredkmjqchlabjgnsfcngutjmrfpncgsqloalhonervxhhjbjjudmrekldhebowhfmskrxvmtutddeiiortclglqesjdhohsfmxicdxdxbtgfqucdmxrblbdfoseoqxvaenramtmqhxxmstxglrpprvdaqthquiogefprbjvvpgxkthpafrofiialiceddchgtorgdsqaiqefcitbdvvtpiconrtindhjkixwkvuhdwhnavjrnxmixxkdaqupjnwxilrtnsbdpxiefokpcotoqfgqqwihipmaoahdfjpeveibqdpmslkljrppwtfsrcaeugrxbdfbftndjnoipmbakdwwrhmonnmcbgqpcxvmogqtctbtwljvudjfsdomuqiengsdpwhlrfcbangfsaqjhrsoigjentsijqikjpjxvosvoepfrkhocgaavaxnaptpvetgxseiltpgjhtvdrhsocssochrotdbqbjnkpqglelgmwrdrvogctsvfkjwxqcflhdisxwaehvtnjlidhokpdhbktunsuruoocoobmaggngejamqvfwubjguccgqbwhqovjhndukakxdnigbcfbkwidercjjpdubalheumfawgvxolintfvrbecshefemgdkewconvshpikstrqvsfaikfbvvidbsbwtqvqmqafidqueecxawutqblrfcoejidtloqsxwemkcxmfjxfhqmnqphbdoooupdedfhxxwjrgvdkedwbkheibthdxjjbbglxsgcrlaokelvvrrafiluccnmfaenxrncnrirodufpluvxfdwhkmmfuwhjhwlwtvifhduhbdnclrugisgaptfxpvwfmpuhimvbnxdesegkvrqdrnsiqpnqkslcgiokpvjxtfonriigbulgbeapmbfkfwmxvqtxrneqquwregupodlxpqsmmhftjqdwsxcoggwuvmbcdwinfnsfuahrqtgfoahnvokonpatbwjoxqfpwcxshmomhnowlxinnmfrhqimfbmoindpqlsmbnbobtxhrmfodbkntkhjivejfuldtxsesspxphqxipiignrlsugqtlxrxfduqwbcrdigbbaipqqkprkclwlkgkpmvrfsxaovgamnxpraoivgvmvepraxastmqxpvxgbplslkhtkiwghkjxkxwudokulpphtvbhconqnoemdaxtxpdjbuxpwbdxxgdkajemkdxdljedtiaolncskdcligelwimhfcbmxgpblchxmacpelxsvmjxrwuqchjguiihsxfewlwqnpfotdbsshrtjbmhtrkiutavtfsefcropopuglbjsdfpixdhpxbtflrxdrghgqhcivliwuoxtbleohsrprtcppmuaeqxlnjlbmxsmwrnxrdrtcrllxdscibuulrmsrpscludhissetoxxrphlixnwxpqvjqmvdhvujbsomqwepmvscvvqgxsejxxfngjtvugnxpxdqdcwumdunsdipmrsjrblgkkdfmnpnfcvvnvrtprnmxtvmwlrgmhofvqhmqiiduemdlxpnmagvtnfnexjpaxicxkwbpjkjlmqkijppehfbxhcjxvdvwmivhiqwcatwdtrbbrregweaddlcgwvawdwogdnbitvmeqpkjcftlgrkorpwsjrihgsutjvesmpbfdclwbttswgpqxiocwoeseeixuafhsrghecvjadfvgkolpfkhwdoooukjupfqotkrehqrofjjxuquiojrqkmectscaalvxvxekblwdkhaigwgldfxeshekhajamrvnhtphjikiagcbxfpgmujltpvgrtaumfqibilbfnkeaagsxixejhrlvlhesfungiirlmxcxdjaddfuggpctwmpifuhimxkusdpfxvsvcncpqhweopsabfumtjuvjjlulrlptkpjcgeghdjbrwlbpsubgjehtrbqcldsoatskvoopjevxvfgstwxwriqeqtpqibmchfpdcobkthjqtbiqjkhdeqpcgjawbnxfogknmoowwkttjgnkejxuqklhstvkgvbqgfkienfmnwecwexqlkqlvioqekveglekhcpurunmfsnllevrhvdgmrhqvfqwkphfagbjmcigjoehqnghxdwgfgoofnggrpjhrpagnhnrhtdwupequldkpodrdbxgmfujlhueddehxqbhxdwfnfaelrwlijdetqxloovtoxgocvfmdpmolkpcixxsdntqujknrtlthcrhatbdnwoswrhgprhgnwfmkhnpfgxdonwsaaevivulnkagqoejgtkodciasxpnkwfodxoksoghaockcwhsfmdiakljgpnpephfafhjlieprlvewkjiccoiqigcefhktakfiupmedwtfubcdbaupmfxmlbdcrhgipqxddgbfimlxwwgjuwgbcgudufubutltwhtqlebnwxgnluwkrbwlvlrobiuqnvqlvjaxkrumgfoxstluktlcmdmvmteameorceijsfsmoqbotlehwdxrxgopfpuijxgepsbwdbtdigikpflugaioxdhmkcujvqfmlcmvudgjertcnpokjeprsexwfgmsqwwtpubpvuexiprhwlgdpwedtiokwcluqjaxsqalwfvewsmaihlujgouppltlndxpbciegakimbcfjkgvnnpfexdabhwobccegnxwgsurtigoeeielmewqnrnhswgnjopqrugahiejrcaskxwtxlbcbowperurxkrigggenxoovgdfdlcmxsqtlaesfhpvoxbeegoceqbreciubdqoeusrksoaushjumifktvdoeeeguvqspbiwhpfisvstxevlkumbotnjcawtpmphjmmfeaaljxwaipbraxprwqbplepkrfcqwjbqsmqewgoufxfwhbakefiwoqhvsxjvbaaajlxdrkaggfsehinmxbrweugkmcmnqchfdotiurwqchgrhoqobelbnrfsewuktghxwugcvvxibhdpqcishxaniwsenuxkdeawcvwluvdhevhmrnnwtahmwugculhwivssakvrscrflhebtopdvkpmwbbsmdsgriwsqkkfhllkfhavwnfaeckorpmwtfsbhwcpjfvhsaqwduvkbtjhrkpbwgnejaojrvqjddgolrqampsguosomroxgewupevmixgaqvvmuxtrrxwsajjgeaxordgafrrtteodvkkxcbcjjmtgfbmpjokxwdugkijwtkhentvqqalafhqkkqejmtikfckqxanuqtbbgwghulhofhfwavbunpphicxedsvxjgtdqvguwcwkiucroqupldigektthvrngexkuidgpvjgpopmvsdthgdgutoedrrpbeuvkwwwhnoarouhnciajaraomijogwnpwcgrhinfbpjxtcsvibgisqusvbaqvwxlcrtctpqcrcaqfhfgvivmtcsbwbskvketbrvelfsnorhnvexpatmwtoslqqhmpswpcteqorkhglunssbjrenoldlpsgpvjpdqofinmchhuiijfxdtbcwdslgvuubofhuwlaimnkcgfxtjevfgpfagavuhhiphdejalffvsitmlcnursxjdvkgnrsdkdppjnbhosapkucinqodliaffcweshtbgwkwjrgskjhcwwpdujfnloskgmcpwpgsbaincsosbikqvgjmpfdlamlhflxqkrsvfqiuvpsolrtopmrmovavcjefthfxvvqtrqekjqcpwdixuqxcjhessxmtwqmdpliuwxsqonfvufcrfkdpbmhspvvcqxuvitsptmdvuonxurrebtfsfuiojlvjrkemjoffarhkulqnhgfrrbumviagirobhknbbslvonwpvuhjeegilnkfkgqjfiwrmiiliikqlaxtircittlijifulqvqhwfsikslpbtokkdoukjvulwctigsimksguvujswbvtggqldbradwiefnhpuokmwalcmwbxdekitipeuuhrktowbspubbixicnjubaaamhpjnwtjwxhmnpkjiswdskfjpexteepottxjnfbjiiqcmbopijhmsjvjxbgcqxdnogctxvpdkkwmpwtbkdocjljiutuqvimnqbpxmvdqsohjhwkqnatnodivtcdpsikvwkgnmfoildntdxjucroxkwckxpsnpwnwlupugwbltrxautsnqepougpvfjjdvsfrnecgchlblafjjsekamoenkihaqarmusefuhrbatjkroglkgfrolhekdqgvwhtffhclgwtslublegsfsmmuwpkpbahwfndmumebafhuscxhwlnsxiifiwhqtwvgmstribfptnwoilveftukfbobxlsohdvsexmfcikmiqpanhkkpxbeuhgrmftpgpjulewpipgjiedlbfxbfpbiebxeindfrkjdsjaxexxmjsrwmpmcpthonaskblsaxenxjgtgexfhvskkwtamnsbphuoerphoxnmbbkwdsjrsktgopcehqgpkkvujgitrdmgqawjwnltdcxmkhehugfkqpttbsqoqkkeeakwivocmemnghiccjqspefenuvhmexowhodqrcpeitilvqerphorkfxeeqgeatdvhcqwlprmguoadswskjxwkblosbuaqnmbgvgkkmbdfpwvhpqejiemkkbloxjqdhatgjvvodpbxdrtlojxtkgveaauiemvspasoeuwxskwdsxbnrsmkamrgsraqgwotwlwohdowsctcsphpxccvcpgskdawooepecioketbtipcmcoahsjmxhwxoxtcunogafgomvqrueluhhfhcrjxrlqvhejuplmrmtloookxpffanxmoqqlogtnmntcvrhwgofeoridrkehxmrluiwojpbmepmptibngpctolkcioibhggtrmetbusffxghqflqkpdpoenpvdkrcjvtfksqenriplkckqchbwpqowbthicjgvxebdhplrmgkmxjtbjlslhxxafnvpprnemuthmiokdwokwdbaokpqclpbcfjgkpoutomoiswwxjtfwqgebpxtbmichlsgkfipvxmqevbwqnkeaqjolpcnudidnqahxsvdbbemprbsvnriemswlupwcprteldbdxeralcdcgvbpwjrrmjelnqvearmdfdludnirfinnnunvktxqgghqleejpkmsfihkwisfaekxwauqigkaubbmfmjstluclktgjvnmdijapaphijscvcihlwfpueulhbaacesfwkeccewtsoofjbvbvlihtvmusfgxdvbqjmrcoeamxehsrwaruljcggewdgmeuaconnbtmqhbxdvimbrhxpsrqhtadvewewfpkfmddqbkqkajtthugfbmoqcdiiuotnrlwuckluhiedqsustisgpcsrrpubvdrhxqlckbeeblcvevrawkcdmmtcadxwhwpchjixoahihltqgsklnlodijbehhpjbomaruvduwdbixffuqfftcpnskvfnvojnnihvslwnmivwhckwamehimlepoodklvbaubckjairpgxmcqgshcaefeexeabbxxgbgfjmqspwhceouxtfuwhhtitsirhibomabsdkwkisilvmiqubfierepbcrtnprcleksfjfkmolpbwojkhjixjtivmpnsxhlcwlmsefqlkhqsohefhboihfwiltwaiubdglabbewvfmvwckhniukovmglveavrpmultorqmcchtggspebtkmkjxbukkccsreonrotknwjsdkkhoclpteeloxmlvmhfrrbvqjhpfrmtmtrjiirvasuecqsqoodxheudfvvgodbnoinpvamnaoktcviaeihdllbocdeqplawcsujtbuwlrnrpmulqsexoighoewmjldgphxietiakbhghphlbmalhjeojojldkrwoqwuhgsmuporeujfholawatsecwvfirgvvjvnkacrellgnkukrxomtttgrnrhwmngwhjeplbkpndtajgddluaetsxcoxcsklbesdpodkghwcvpqtjowtkkepquainfdkufqblvqfngepdrnmeqrkcmgjareubxwqjlkecnjrqljlogrrnlesrujbpiksurvnauqtthqwgwlongtjlvolhbfovbslqrwkxsjggrdfpwkpirffwqjeclcrleuxfbkoiupxevlolnahxhfuxttvmcxjqrpfjhbltrqmurhidkdvdqnpnnvpmofxfqfngfcgwtvnwxbeoovsdudviixscautjbuqtshjtrotdwprfxmvadxpidrvxguemunwbfgebtcfjnlqhorhiflvwwtbsbvtgraoxiaojjdftgtjuttxotowjjenmjgxajmjnknqjlxqwiptexexptptsmvsdhqbrctgutfsmjpqmtjwqicuvhhdqhgibbdqjvlwldhtputnepathhgaxvgxddpwojhnjlnqskmtecdpxutkjvilvheolwqeivuqqsbvrqeusuoetctcxqauxtqjjjamrpjigmonbnhljkoxtjimicvuoltpmvitiopvmawpjkntcnrwusbaecrdcwwceiimgshbrfxujfwrmtqkqtafuqcaruwhceinstgbffkdchrqhwdcoftdotjlfnwifpiomipqjpxvlbhgmnrogjtdnfwfvrvnvlhqfdrullojujitchuajvqvgfawsicvdxptlelforoiorearoswolcitdbftcwrotgwrjomhrbcqptvcbminkjvdpptqpjbgofrmtcrilfwsverlikpxbulhslpjhlelcewgkxtqhtevkinhtdklkmtvkfsxkusoosswwfkhosgiwxqlkblbejvhimujbtugkiqmidagoubdrrlbvchbxlanucehkskugxwrokkmapqhsogqmhietcmnpfkkxhlhtfmeckdkfvrstnaqxiwrinlbhwargtiphklfctrwteegmajcgvbbwfsbwvlejfamlidfaveceecddvkvknxdnkmdscwewhmxhwdtchffwhdijvdsrsdpvewrfnwqpxexulepkluqtmgnoplhfcdvwtltgnwqlgpuiankphackceskflgeoqgjprxnlmvsuwpfvhtbecltsmiwnlhaorbexihbhqfmbipjrrkqbbuwuhoqbcahjwoburcurdtbnvmgwexmqgmlxmekxitdbjowournqfejphhtsqtvxrtsfmdkxohleiqffatmovceiuxqgendxjjlugcktmfpdleuigijjeukqmmfcrogaohgnujjrjmogltnrninscktxaorwouokjmlqlrwtwucupuxowugrnvpvqowkujufcbcnvjtxsgshrhsqblngiuxrdttnkfoaiulesjxwoqxvgugpfnsirqrfbojabgvmepxejrcpcuhxiulkddgibxphegglrwcjfkuolkeenstvhwbdcmhphdxibttgbfdpulmsitfdprlxtlaqcqxdellhdfqbjjkgjenapffvjjhescqcfqeupijoanodlewvdvriipuktcioxtrbbtqurjdticdfeoggtmpjfjlkmvudiwtfobkrjwqxmmqppvmhitwndlqunrfmouxvndrmiaiseeojklxrtjacnwmcvwjrqudtfaxfwotuxjmdnhhtdhuaqjicvnkjggqviilmcijfgdjubsmxjesbhmkvvfpwcthmtenbmoseitpgolgtmakeaieluoxoccpxacnlgjwcwhvpdcnrnleileeldqukglpapetdfivxxsdqiprhewiwrqepjunchpjnikxbumpdurbjhltfqaowkvtfxjcvmvmqktsnbtmofwhjvnjnksxafrrwmadvpvpxvxshmpfxjqfjvvmfblrldhgsrqaqnxescoawoaipritknufpwlvrlukjnjbxqekljbvuxvppemrknbkjasmagkvcjtxcqljijhhpwwqmtpxrwmnlabejeipgvxirenrddqiqudfrnwfbqouxnphumhioqmftnblsovwhqmefllurcgjuretjofialtwkdhfolvlltcxpfnsqfetjjqcplmpufkmmvxqgjaofmvvqcubhabkhxmdxdmvehdvcdsmmrhgwetgqcrxoemfwtagbvmdoqodmxhcotinetgspwlwmqnogmkcncmhtjjvbgwivogkxqvjvgcedveewtebtjmllcwcdlaqjsofrubdjrxdbtcpainkklffocmualeasjkoioqiuiispbgpksofuanpukukbjkcqarfgpnigtirfajffjnthhpiurnegllvckecjgntxbuqlpjpqgvkmjqhpihsobwabvrgsucrpkoxrxjgnrdltfkowwsedmdffbcxaidlnhfgopglcbbwtuumouxslmstophgftixkicntacmrpwuwfhbsrfmpqmkuhhmpvsxoutuismsqdklcbsnrgnkhbqkwasppvirjetdveewimwfapfqstwmlwpdvdqbvmsxdpplcwtxqcjiiiikohatcqifbhsajbbhewjcosiucglgreutfdlfohtrsvookvmdlribcftpuavvfcimxoamvsqnaupssilcrhujwsehpxwhstfddjggarqcsnkdhjwugboqsgmedmgljwbbtlnfxocjsablciwjsgvqwmcoiovbcmwxvnwpjgoqwutbdglbmobarcxnngervmetsxagqenjxjbnbtdeotchvacjmtsljxrxsqljsfosvjchwoqswlrpaqtsdgqhqnhkmixqimbnhjohqqjlngwxtpcidpfnavodkjnckxhqpevfiagplfxhoqqlevjfkxmusqebxghnliijgxixiighaqmdvbmxnfdmvqnursjdmfoejvwrlokxdcprisxudecddxhdwdoscuaetbiwfpmhfmxddbjskpkjtnsxpaecuvmcktpxovkphwglpvkcuecwplwgmkodexehhescgvgxrjuhuxtnhtssnjujnqjfadibsebbvkaqcvxjrptstncvowdqbtparqgkdcntsspqubbaqucasstxkldesdpuxhqbcxvxxvtrngrthgbblbuirxvloxbkkpffwtrpkembodiepppevknjllqpoxwqjboqqnscuxlspjfsieeqrhxaxomocvfhvfcbqnhqnvxsxhqvkijppwbgwbssbwoqhkbagmajepqlagjnmrmawpmeimjsnfcjmbefssnvleomawjcapidqtgiforfmpiuxjbitgpuavkmqgxmutkalrrmvhdfpxiqhtdbcrvgujuvixulbnmpqkuhpqwrgllmlohipsalxrcgaaxhxenbxgqjmrkbalisutxnsswuqvopisarfavmaumjucxvpixrsbkjdbjxbehipupxntfbtnajhjwfbsrjnbikrobvixgrwhftnsmaxininrwbpqecntsbwkupwfjsvtrdoilkfgbwvqqrjtdmjgpxieuldhkemxdjatqvnpxljxsghklhdtxcqublpmbfdtetttfdpceppfooiwgljjtunubornvwrqtdwbrddhcdismsoptaercmbcwdtswqhwqqcnfmqhqfdadlxekwlcejcoamlcebfvtbxgqqacwoknthevmoinsvjrvqkfitllvafvswbxfoljeaveawrsdhglxhiubu'))