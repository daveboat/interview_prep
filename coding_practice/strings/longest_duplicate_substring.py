"""
LC1044 - Longest Duplicate Substring

Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The
occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the
answer is "".)

Example 1:

Input: "banana"
Output: "ana"

Example 2:

Input: "abcd"
Output: ""

Note:

    2 <= S.length <= 10^5
    S consists of lowercase English letters.

------------------------------------------------------------------------------------------------------------------------

So, this is a difficult problem, probably too hard to be a 45 minute interview problem. To start, the procedure for
finding the longest substring is to use binary search from 0 to the length of the string (N). If we find that the
substring has a duplicate substring of length L, then we search from L to N, otherwise we search from 0 to L.

The hard part is writing a function which efficiently returns whether or not a duplicate substring of length L exists
in the string. Before we get to that, let's talk about the Rabin-Karp algorithm.

The Rabin-Karp algorithm is an algorithm for determining if a string exists in another string. To do this, it makes a
hash of the search string, and then does a sliding window rolling hash of the string to be searched and compares hashes
for each window, only comparing the strings if the hashes are the same. The key is that the rolling can be made to be
only O(1), so the worst case time complexity is O(L*N), if every hash has a collision, and on average it's just O(N), if
few hashes have collisions.

There are various hash (or Rabin-Karp fingerprints), the simple one I learned is

sum_i=0_to_N-1 ascii_of_letter_i * a_prime_number ^ i

Then, when we roll over to the next substring in line, we subtract the ascii value of the character we just lost, divide
the remaining value by the prime number, and then add the ascii value of the character we just added multiplied by
the prime number raised to the power of the length of the substring minus 1.

For example, the hash for 'xaby' with the prime number being 17 is 24 + 1 * 17 + 2 * 17^2 + 25 * 17^3 = 123444

To adapt Rabin-Karp to find if a duplicate substring of length L exists in our string of length N, we do our rolling
hash computations, but every hash we compute, we add to a dictionary with the start and ending character indices. When
a new hash comes in with the same hash as one previously seen, we compare it with all strings previously seen with that
hash (hopefully there's only one if there are no hash collisions). If a string matches, we return True, and the string.
If we reach the end of the string without finding any matches, we return False.
"""
from functools import reduce

class Solution(object):
    def __init__(self):
        # self.char_key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11,
        #                  'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
        #                  'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        # self.char_key = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10,
        #                  'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
        #                  'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        # self.constant = 3
        self.mod = 2**63-1

    def hash(self, string, constant):
        """
        Return the Rabin-Karp hash for a string
        """
        return sum(string[i] * constant**i for i in range(len(string)))

    def roll_hash(self, hash, prev_char, next_char, string_length, constant):
        """
        Return the new hash after rolling over, losing prev_char and adding next_char
        """
        return (hash - prev_char) // constant + next_char * constant ** (string_length - 1)

    def modulo_hash(self, string):
        """
        Return the Rabin-Karp hash for a string. Based on a modulo hash
        """
        # h = 0
        # for i in range(0, len(string)):
        #     h = (h * 26 + string[i]) % self.mod
        #
        # return h
        return reduce(lambda x, y: (x * 26 + y) % self.mod, string, 0)

    def roll_modulo_hash(self, h, prev_char, next_char, p):
        """
        Return the new hash after rolling over, losing prev_char and adding next_char, for the modulo hash.

        we pass in a pre-computed value for P
        """
        return (h * 26 - prev_char * p + next_char) % self.mod

    def duplicate(self, string, L):
        """
        Use a rolling hash to determine if a duplicate exists of length L in string
        """
        D = dict()

        # hash our first substring and add it to our dictionary
        current_hash = self.modulo_hash(string[0:L])
        D[current_hash] = [(0, L)]

        # precompute our constant for the rolling hash
        p = pow(26, L, self.mod)

        # enter main loop
        for i in range(1, len(string) - L + 1):
            # compute current hash by rolling over from the previous hash
            current_hash = self.roll_modulo_hash(current_hash, string[i - 1], string[i - 1 + L], p)

            # check if current hash is in the dictionary
            if current_hash in D:
                # if the current hash is int he dictionary, check the current string (string[i:i+L]) against all
                # strings with the same hash in the dict
                for start_index, end_index in D[current_hash]:
                    if string[i:i+L] == string[start_index:end_index]:
                        return True, i, i + L

                # if we've left the loop, it means we didn't find a match, so append this start/end index to the dict
                # under the current hash
                D[current_hash].append((i, i + L))
            else:
                D[current_hash] = [(i, i + L)]

        # if we've left the loop, it must mean we didn't find a match so return False
        return False, -1, -1

    def longestDupSubstring(self, S):
        """
        Find the longest duplicate substring in a string via binary search and rabin-karp
        """
        string_ascii = [ord(c) - ord('a') for c in S]

        left = 1
        right = len(S) - 1

        longest_string = 0
        longest_string_starting_index = 0
        longest_string_ending_index = 0

        while left <= right:
            mid = (left + right) // 2

            duplicate_exists, starting_index, ending_index = self.duplicate(string_ascii, mid)

            if duplicate_exists:
                if ending_index - starting_index - 1 > longest_string:
                    longest_string = ending_index - starting_index - 1
                    longest_string_starting_index = starting_index
                    longest_string_ending_index = ending_index

                # look to the right for an even larger duplicate
                left = mid + 1
            else:
                # look to the left to see if a smaller duplicate exists
                right = mid - 1

        return S[longest_string_starting_index:longest_string_ending_index]


# based on this code
# class Solution(object):
#     def longestDupSubstring(self, S):
#         A = [ord(c) - ord('a') for c in S]
#         mod = 2**63 - 1
#
#         def test(L):
#             p = pow(26, L, mod)
#             cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
#             seen = {cur}
#             for i in xrange(L, len(S)):
#                 cur = (cur * 26 + A[i] - A[i - L] * p) % mod
#                 if cur in seen: return i - L + 1
#                 seen.add(cur)
#         res, lo, hi = 0, 0, len(S)
#         while lo < hi:
#             mi = (lo + hi + 1) / 2
#             pos = test(mi)
#             if pos:
#                 lo = mi
#                 res = pos
#             else:
#                 hi = mi - 1
#         return S[res:res + lo]

if __name__ == '__main__':

    S = Solution()

    s = "rrjznqfweifardpecvejwywvabszicoeiyrnbmquhwlnkkjxmtkevfigqjzbrxcqqskzbezfpfeimuastbalawuamduzbywnpamxqavtmozzzjauqoyknojewrpcezddnpcmnburkycgehcfnjghxxkmjfmpxixwpboqttfxxsusqemsjtvjgxtmrhvzahundluvpcppgtyiwiwahkchlmenvtajimldgegqmozedzchtgtmhdbavwajtvxfzwishivqzhokfvdwiwaammwhovtgzgnlsdnuaziofeprwqzrmlrsdrkadyuqmgnuxptdvyatnzrvxtpncqisqugbixlssybsjyzfofxhmjndytspxepdbgekvouiqzxzgettnpjhflsatmqzbaxrofrnzzsajiddpohluluifikbqjxosgrihksatqilrofpvweghrwsnaaqwpsxlldtslfpyegjgujihuissozbpmendfwaalrmhmilzlysaastocrdtyamkkgokoldneghlcmmjhhxtbngfywamnvfphnwprknufdrfzikvmnijwoonwmdbjvidkwszydkynaglkcokcnzulfkpmzqpgtvavpvsovoxqrayjprjtfbcigwoppnolvthhqhxifzrbkepkyciqfgredfkbpqvirjingakmfhvyksilxfwliyunqsayaokqacqnfktmencmeaktwfnsifiqsgslwayclaottlwxsvfzykbcizckostornvmnavxvuhilqytnrjiannjeptcnhclypplygxwafqxskfjimtudbshouvmjwxwkevwpugvsgdemhmukbetdyebhxwjgmckxcmtwaynercctniwgoodujnrfbvhuvhqgydagxlrxyspgejawobjpchkoowigbdnorevdrtmxfvohccigwyrtlgqskchifeklvdnpoybeizziqskdblvatancyiwnpjcddjcodsocmzlsanucfgxgsphpkbkcrmfzrnukwnwfqtrwqtgepahkqnqicmsckjqdeafxsnihesfodutrsdblcgvkuilqwocsvntafqlvhqpcvkbleavpeoczlmibzvvtnwzxthoubjozsptdgkiyggiiaohdfpqevjhkquncfmulfruldqodisszsztcvydylvdjygjvalhbunbentjkjxflrrqpczxthfxnqnprrmxofwbllsptadhhoxupnysaweltroygjsoeniekamahazzdsxjaovqeygeztfxoaegpekhouelllnzhnkggxlszhoeacsukundrkynbqfgvknxoeaxficohlpbyijuckkmvkqjghurfcntpmwzgwfbljkzptfvbphfrajweyqkpjrgvcqbqsvhuqlgcmbvcmdgtevavzyoirzkucdwjvyyulrdexikteioirdcpnhtpntsssuhnjzpsskidjvelzlsntbbfxnkcgpecmkgzexuluvtfmseniegbynmmnfansjqhpwgwwcmrmrejgryfysbfijmkktxlblhnlxzgbuzcwwdhcmpjvlrpknbgnsropprswwhxgnqppiglsaaooyctyxwgschsuofwvuehlbujusjigwdvgbpjwzsbaavtsixtlqhjyjxslclpeofczvazxzcokdzfbmmjnyeaomodpcggkrwvyjvurqxrgmzocebftnjeksqaxlodrtgrueouuoqrxmbxntwrwhmfgmqunfmmceiltrrynusieakqlzqyrhnhhvbcqtwwnzndgniqwwdqbdspmsilmjnbunpudfiqsczsclfaxzeydyuyaubasgwoibnhoigutwsddiznhjopfmbkdnssiasozhvhcgscelaugvwbqhxwnimybtncjwnuhznukgormlydozwrgqihslyyosjslozgstevxluedipbfprgvgaadzxdsiqwstoukfzltyfdtctlklyhmesablspydkdtuirueaybqlshtmxaejlbpbmvvtglxriloibnkadicqdfuaevoolwxwrtwenzulpbsohrkybypmbuxyhounroyifxoaqmudiyzuscbzgckvdqvrwmmolvvdamonsztpoggtjqjkndmkpjkldelubszsbfvoyjouqudshlvgqjsfbfuczfoblzmymbsuygjxbtdjnwzjhjnegewrlzgitmkeyprbybddxfmxdjlamkdhrbaabswfbbhbwfcnqdepgtlcdgzujkvswfvzsbxmuuyfgvudtjrjfggjdgeqoupodquhvhalmkdxjggjlxiyrssklvohstoxkwzogzurlmpurrqdixpnisdgzqepyusnynhnriuhoegddvcnyxyecxccdjsbtnsmyrlerwrrxlhheznrjgpgftzstytwpfvueflgfrwxuimksrytrkgzpxfkmzvnaacyethopinzbahddminhbfuqihtfayboziwmmqsihtjkhqbynnidyenvhirxkcmudyspopbawisdjtdwocwxljspgdhrajdhsducnefjjrybscwzmhpgqcsfavhsexbikomjanghlydarnciaxaeonbhiffsaejxxoijfkcqlsjsisqxkyddlhufcmvmasserezowohykdlrbbrflhwxpovnvpsqgvkhsdvgljawutjcdaubqphsjnvwrqledpksugqyegvhmpqmazwvjtaexizjvscrtayxxikiydjqlxvvetxwhqrptixhqblspbkpvphvmdbxbjnowaaezhyaftqcpyyxtgsedsgncswurpbdwbxbzbxosfnajndyduszjltocuxgaltqsouaallmqyfbifpcxfhfbsazcvsqwykglcpgxcrbvkrfraarnihkwaptmzqykaspvxugxpmeedlgwsafyrndldqkvaiidlxwsoowclmtphwxogjtjyifwbxebuzzkadwlkjyaqanyqqaeidcyvcmszhywdiudcvzyhqtvqyocwbyowjafssmosisfblpeavtvbwaicisxxlwftddydqknbefgetvtmgwleuurgkitvyykopdtisqovvrospltbpdzattmxoubypjghfrvlthvddatxgtqglkintjuqsrjegrvkrejqkseizdfarhmqnftbjvutfxpgiyeueevjzdyonjizeaopzkfzwdboxmraymilyqaofvgwlsyjydtzctfossgqkqylffhjlajxzgzqjeawceypkskyqrbrddztqvsfxqjgitothsxvvmnwfmigmuepvkdphcwpkzoctbtlcijagxdfazldlkyqmkkfdspwgnuzrwmzeeqqtsvbftlpljpenunpplsguzbgaqifxbgqxwhtbxqbmohqeqzdxmwmypegpmfankhmenuwpmbhbuashjswofjssdhljvruwxaqysjkoayfybrinsgfcvmtqwocnteezwtaxxjzbbtfgzfnwyppgfueevcsgzrrkwfezqgmufhlrxvicurfwzogbwjjyahktzqntebnsbqdluhwdpvdsvgstxzjcibqehiuhmcnfqrpnwsrdyuzbgixknradddwxkatizkihquldcjasogljloacmnmwmijcoqllzgrcnztwigkygpcbwpazghvyypckpihtmqoiosbizqacofxrkjilayxilyutjwdahiimbftyksuyryworsyvdmndssphmogrnysmmhxfdwwqjfwvczvtvhmrfoeoypsioalcqzhnvfrmkcdmchrjozwensbwneezfwgguxjnaakvtslejzlyvhyqpbtyrpqsnaawmjyekjsrxjwuoebdefcsjccyvexgtwidclapqfgielcbzuaotbtyeelidppbagnfjnotfjioywkygtsyucttmrgqtmmnrukoeupnwienqqidasxhpmfepyzgycsffnpermfgzixeiunxolapwjrskazkslbuxsqlcqjccieooxuojsgbdozikxbzjxfitzwjmcmgcponbbjwrroxehxjtsevvtkdhphxxgwtixvgesvrinjkpyxbexzksfyrocjbnhhztpcfxqsrpnefeerfkhxloiodwjefjpffjdlfgvwvnkcrpdjgjbrviqwechveimuvgwwmaqtdnmibpvjogmfcebpgjfuveepvzvizltfqjyhjgndotxhputffvpnyxglyphhvvrrbhpjusfpiuigczuyyzincvmankvhdbitfmlikwprctztjdvvjnlvplqniinjkgcqxdjpflwenytvfcvogluoxepntiuaukijtyaybjagerakylulrgqdjizoytttwzkqenaihavmdtkfhzgopnijhzylbbspyiyxnzmlvodkydplnwdoezglogumizxoonciavhrmgktlmynkgbebkfyfqsnienkuhfuarfdxbrfnswhsqdmjwqzqbbrewosyorgzkllzfxilhummpbwfldajxweevsqnygucjgxnwmatlcychmmltnexmrjfotcxwvwrmwylzokrrlociiucqtzmlamikcbqtolsxszqgvzssgbkpfhexssmthjpbopyxfwhlxvwfbdmppquykaveibtizeqakbhkddbfmpfgzmdufiahhvismldiftmwexyfqpcnqlnhyvkhpvxrqbwcjzkiiizprvfykzfeblhmodncrcnzjhtkzkxeoidhymayazdvvavtnandsdqtchwavcagdfwbjsldqetyxkjbnxkivrgvgmutwjfoxqvuhfobmodvcfhpoznwqdpzqyuwoyaiibusdgvpyfofpknooabvujeafzxkiqdixeajemlybvxntdativywiidrwfixrybezseiwvgqffdpqnczpipiwmoowethnzisjvxubxyzmptkmlngfgcxxnddsmdrpvsypylsjznodgjyggbzuhnyeeyjtdbqqmdenazgfdflugcibgekeaaeimojnhycynngpdjyffhirhkjsnqbgxbhzcrbwcnhyqobdjdbjavmlkrzymxtsindqvijpsknfezfpoqgaehiihsgpguwufwzkiuxajakmhqwvitcjytesbubaevjvaldvgsaobsybkzxujofncvicwhhmlogjrroecjdrwvqwlwbsvgnwhcnmwmovnurwsdjdzzodqurbdbslomdrvmxutqfyycjajwyfstzomtbvolaquxgfnasoguyylmvkokcyertmcdckgkdvcweykbxxzjapndpnmgxixtzerpwusukqbmxjhsdltekcnbhwjbgtiejlievmnxgmpvoxnxgetjaknbqhmowejqpfrnnfydtvrssbjxcjlfkdybuhzyxuzstwphxwgzlzdgtlwgecgdbucouvtlbouvcetmtkldznaugjzhgodwgcjtersutcjkdthlkjnxenepyiffdbunwvmcebngkglusenbjifrqvwzjmykltpiluddzobkavbbndtdiqizluajtdxjwykmhesfchsjqxrqypvccdhujwyitvgbfufynxkwvpifvwtfosxekvmknvutikigrkljyuorsxnjpkveacpyafyfofylmyfcwdvkwovgiitkcltruyafyzvnmvggedmwylpzneqzfxwrnximfpjclbsunrsnbfbpmmsjhwvqgyijdszefeegwjfgghocjynfaitlwtqcrljyewjrmamwrmphyyufuyydnvqeemeywjdjjjzbxuristvgkischnblduybaphqyajdvzuecpcxknqnptnlfrzmixdwojxidpszquqcemjuuonkaedzqmtaxjpgrdtqymcscawmdkxtsflurrvyuymqgileypfqcvmvqmkytmgjlbhlykhhutpzsatdromtzlopbvxkmbqmuxibmgafjsrjktgmpzrbrguolhvsaajynblualwewyckqbaebcvmowfpwnleskjqyriotbkvpzpbyppbxiocxlfhpxadhxsdkjwjssxoyaieeofozseljhbknqnzuzkxqbptklxxcxcipqskojeswdlzaxtpdddosasnjmoosjimgvzclvrniszrnhbchnbwlbprtrmpntgnpbolctgkbmjfxcmhgciygsbftflnxapkwmoxlymlgdnocrxgqmltrmkvowhimxbdftzvjmrkwrzhphxmkzcxqxfxynezjuqzpwdkhmxilckbiowtxxaswagmtgtxtlbwrwfvczrxvvaojvnurgjpeqsawjjzklbejllbkvihpwwjwnqckzmacmyhziwwmtrrhhgnhltuwvurxtorbppudzhvcbdyiqsdwhbpyewscpwlevrweitgsjocwhzkzdjdxfomymsltsxuedgcuwjejyihwsaxrihpudmfjkwspetcogdpxjxtafiaabtclopvtxkxkrtdpmparsdnbhdyytgiyuakwmapdeqfiznkitcxlfkwdzfacbwstpbjasbpykyxovdzkkiiunvklpnqugpvtvmcvypkshuajenapzuymfxsgajznkvxwknuirmieiwpmyayunfnoctabcvdvkuhpqguafpdbjrhiefdmrhahvgeqbabopfpnzhttsonvygrafdlrngqkwpixmfwmnusmcaboqqmkzzbuederuiujeljeiapttojqfvlszplrdpkmfpwirjdkijvykapvmgmeuoitbkgufbpszwfznucfmkdjfogqqfqhkzjfmovzfvpbpukvmyzwloojwmdumymvxqpzkkuzvadmfmdiylxhkwdwqfrhvmmqrnjylzxhtqrmwneopqppfmfgknfcrecaphhgnimdnjczvqkycwjknfuzveudjtruvyozeiwldkzzebyykdzdbxhwlcdnmqutxpvyjqzocbhkqheywsododormkwxcabfmsdmmvltltvwudbxcpquwhheqyyjqqnauslujyjroauhgurufgsppvwkdnwpdjmcvjzabyoblusmrrgrevtdbkaqjdpshcfgphcafpoqavohkphqhdjqzsvqafsfvlmhpgptvaucupfncmwswgrkfhjanhtagrkjotxcybedjbsxzcublfjyxecuaazcawgdrffezzmrlbcrwjyooyexeoezxshqstcxukgbtgeqtwtaevdwaimplvqixdsihmobuyorvrjmtyuanbkvpprqpojbdbnesqbgeactzprfnfgkzwrtocqzhzlsinyniizsglbazxiwheinrddkbxfbvhlwixmwzpgqcpswoowxerzonlqdaymwfrqfkqunrguwbhnjyfbkypgsdpaiirqpyewvdgpzjsnmqmlqnkyghlnplthlxuwlfqostumuyqnnpmqgxzjwwhrvtyqexqkqzgpmrgcnhpqguoinjegahwzsmjfpqbpwditniyqxlezhbsvuobzarhaxqhlwxksqtsodzaqowggceqwyjtismknqrcjoeaalovasoogbicvofptpsljvahsmwwsfpfqlffncfocmmzpfurfrsmgsxygkcgxnfrxhaqibjapbuyboazsneuohlneaheevmswiglllaoplahzdlhbmqgruvrlsoakdyapqadkzmyhpktqgqlfkggzygpwjcoxjapbfyprnfrqghbwgtjgqpnpiuxnofarmuxloxwtjlgnscitqynxbdtnusobpspuroanqeecwgjbleocavkxtarumtjdlehbmzmjpzaxnovhgvmfgcmbenycsaumyeqgdnbumxoduumnqiyevemyjhrxtvovxjfxhirywxddttvseyhtzacszyjvimfcznuknipqfhaanowraxkcqceietjtvjjcoaijxujdjmkgyiiqksyddaysisuhstnwbhjdfywpdxtgcnvgeyqifgtkwcvoqxdvgdkmimylkosgcrbzlxoymstidkririwqppvgaxceisiyfuiejgaxqjtiayjzrowabuvfjncrnikgzyefgwnfclavbxgqiuhihqrzuoqxijnfwvlqimbrwdazgsixkxnimwmeszenkjqjbrvoouwrutxjuekgirgrcrrevaycfqayipsxkstqjxhgazcrlmssxxdgzbgekacygzgaxwyvkwkphmjmikunasrurlikqknldlrtdjmexqwavmhvybufafgshiqjposozaashnnzcvvqsdvwrsrlsevnniiakuoxdpxwiajpeztdveperjxyudrmwsgjbzobzpnzmxtklambjajnlbylocfnvwgxietroguigtbtepzsipmrxkjzrfvlcecitcjipttroltfvhfvgovzlgkvugosvjmccyzvshgjktyfmwyaymzwsgqfvpejrvxbtkvaboezlalqyobnrhrwnuekgsgasyzypjkiolgbgxfsurkxzuiysmwvylwezurbpwunorggyadughgtvulanycfwuliwdetmpyvqhqtfsvaalhbiouaojifydlmfgogqkrjuhkfpyemrliteervghsfztaujigcjwyqqhizgdyulrbpxplhcqugggdvpxxultjudqmqazwadykmsmevijgdzmtpfdpkvfcslemhzhfpxkrfyxnmykibychfhwqlkymiovgkkhxvriwajdapvxwvursvsmuxvgqefnkqxwdqqchhynyxqybvsdxrmatrklgvzgpgjnluncmrinraxykooxplxhrkffqdgqgylspgyxpyhsalqsdxpgmieyeqeyhgyzlfrhckbpktlpcevlzfqjwbmhhmfewcgehfwmlztuzfzqgpphydzpeefuzvunkroieqcbvmemjwmeqkxycvukubbxsmsvrvpkayfmzsmfwzogsmxawoegnkjdtkpiscibrhplyqkyrrrqaxhoaxwanvwreumexduraceobadgajezsokhxhuljxxywganpwyipzmjvvfycumcvceolhpgzsjwdbfkqzfetbyypdagtfojeybrmkxcoyfpsegvpnllyzxtogterbenqpgmajbdxtxbtoasreunoclynosmceanyzqhzwemnjxlkgbgdxoctdsuuefzjtjgzzlylkwsbtzltoxiqpifmsizaovslncvpzxqokyvuppnmlnljefadarlxubmywkypzncfsqxtnlybewnvoubbmfngihdknlzoafswxcvrndikkehtmqhgfhatehjlordlwukoctxpzytjkbwwqinekkhrbognhfpygbmhiwxiqozebaekafsfhmmtkafjncawpagrujtnqlfljcenekwktllijqmshafrllrrfbtovivsljjwsasrmbgvnbrmhbmmuoxtarbixczyusmfcapvyokhegngowjqtwikbfpjavczpmxiqkbtxgbhfgyelolywvlztkrggzcaxrmltzbjhsesgwmndfxtljianmvpyiorqpkvnvgfboftsjvdzkwzgwyjwndhenodjfugwmzzxzljakwdmstqlqhwflzxuvyerezwpxsjokdnhwqfyvgpknzryilmuygcnygsjmbndbjxijtjmnsmqquweawsmkejgqftqybdwzekzqjbspyfphqdkqlrjebsaznancsbgljirduhguqhlusyrfyqlzoiavnmgkcvqjzmuyqfmsbyaadzonwwaithpmpoisfwzpayyytdaiolgjzjvkdjquwjsnchhwdvcgvvrukvwfjbgnnzfmgvdubdydlkolxyurzfpospzvthecghvlgbzmeqbaeswaogwkwybknzkcfbkgxcmduonxcmalstzrcewfphzflzrphjuzcwjtxdnpzqppksdgdsnptytxyzmbwqaydxoyzyjgodycsfflhxgnyvlncscmdjurukyqkaiebpvenryxmjczzpznoavwkfjqihghptrocnamauolbktgtxupzcoksvxxerlwjiytgjmpovwpramhwzwqhyqzgjinjwcmdfupqopjraenqvhyvkxioppmppgjlwguwfvppcoqphnwgvcrbsjqcvohbqvxfxmmezlxmmsjgjnjbcpzuywixsduahuomfoeqynlwervlodyrynvbpmguukqovngcajnkjteyiyxuictlrmkfssipxsokwapzgiubfamlwvbnyiafhhurbewgfsfeljstcvhghxwaecrjbfmtwylblqzayshkuwdgorwnmbelscohlckggsmrnjsferqxsatpdfyqfdswwgfcubyiuwvnywozjizwfztaxkgljhsbgakxnemxwstswronbkxqiggouzvebksmetbqkldintduzherowiieglxtbhgdqfzruwltobfnexvweallpwusahhsxecszyuvmptdjgqnsaclahqfhgmdrkfwtdfufmsdcepggaufqdmyafyevpvabytqcxcebdxztsuhqzxbeiopoglhgnjsxhdizvpgfyxqvurijhjrrtnsblwevnoehvbalhatgaxctdgdjhbeqfnsscpvvucfycburnvgjijsonurhtrtcffbhbakqgajqcgwrbaornhpzyssibhfkhjtkwmghtndgirooetpjcmflwgqotzhnqkhkdxlbginnkywzjghvkgomyramuuhwehpvahklqtkvcbwzvutimrkfhercphbjhwkpnefizfeqpgilvngkzypsyzwxcbtljzgatjiicziytndnvrejbzpdvretswcxcckyzsnymbqbglkqlttdhycokhjfhttlkvmpkblsvsqgtrvfdmcfdkaxptwkhtcczjbazzuejdhplyffqfirrfxroipsrqisbruhfgtyhevqrcezlsalmxwcbzhnbiflewaegmwmmieomnhrryuvrwqxfctaehptzcextwdzosprojqggqdpgrndhcessfzkeelcugdxdmbkpxyfosxuruyeneyjbhxdkhqyxswzqbxufybjvzhkzrlpnwwgswuegcirfdxkgugvennrpmbvmbshmjvgokgoituxetpiewcfluosuywfyysbxgizribkgikqfwksotahknkprdpaspjstgievdnnvjowlclhouistajyofdibyizidmzhueaiyrzoufkjyjopzbwetlxplrjaxihpvwnpunwyhieonncrnamklwumikicqyimuqljwctvaoswktllvikwzfboxvzhbgeqjivreskcdpnddhprnurjvdiopwbhkkgxvtyfnmjrfbjhfedypcndgrmjelymbveguvzrrwwkbwbfqyqmnnsxhewvzjpjlcgyswjktyknfseuwuedrtesjvyscgmpliovwbmzurrklczwbjligdfgcgpzrxpmwzspkqhkbwvjpnvbuapgstuzdepjhohnxmqzmcbireqjpboemgalnkhovhhcwvnvkbrpnyqicgiqydnmgwdhqlxoqgtiglhsyfzxrsouuzwwzbdlgpqhdyhrvnwylelogibiipysocmoypvkcwxpbdwadjfwctruajkntscppwgimcaoxksouebzxfsqfdklsxnkepbeuumokkczdhnvkfmvzqptkazhtjqltqgnsqmorcuzsvrfzuyptxjzkrohzfohgoxchvxcjmvtmbmffbgvhdutzlbiqbrcccpokbbcwmemgfaqnuznixhgbqbmksvsuihgcxkxwcgurgntxneiwqeuloibpxwphystzlivawnkcnfjoxzrlppvnluibgltnqjvmofybgkjhofzadtgmbgxpzbmoncrvpzaqvjqgeefjixzpdpiotqzsrsfcpcqcbfjzxoafqmyllrcqmkwsyqeicvmbbhxihbrrgnxnrrfponqpcvoghesrmvefktrbnyrngmnndapysxvmomkecgzpyrlmklcjohzvoftzzhktyvcpqgngaoyhpmjeejyekzzwvhrmjtytjwenxpabtijtpahjeuobvxyusypdizyaguryvlxjwherjqaxfcinnbgtmymduqhcylvoceedtrgezyuthjesggiendhqyninfhjwemgnfqwgfkhrvblvchfejhmipyjkpwfsxyaqzwutfyslmhrvvdflhczadoiphbxrzypdqxuisiikpmclzdxawojybugkxeovyjdilyxluxkljiaxsnzibeusapumhttvawcullseibwlnjtdgeepscgvwyncokqadfrixgdeoveakvhhbzymyeatxmdrmxzpshtnmhkxrgzrpevctzyeqslsalermdvqlyrzhwwhxlynndturdtelerywqlxhwcpxwzbtsfufpxgwmdvfnbvrxontexumoyrmndkfnlxvayturtagoxrmhcepnquupsyrneuvvnhtjdnqkwpofzeveywoeiagljymdhgrrjznqfweifardpecvejwywvabszicoeiyrnbmquhwlnkkjxmtkevfigqjzbrxcqqskzbezfpfeimuastbalawuamduzbywnpamxqavtmozzzjauqoyknojewrpcezddnpcmnburkycgehcfnjghxxkmjfmpxixwpboqttfxxsusqemsjtvjgxtmrhvzahundluvpcppgtyiwiwahkchlmenvtajimldgegqmozedzchtgtmhdbavwajtvxfzwishivqzhokfvdwiwaammwhovtgzgnlsdnuaziofeprwqzrmlrsdrkadyuqmgnuxptdvyatnzrvxtpncqisqugbixlssybsjyzfofxhmjndytspxepdbgekvouiqzxzgettnpjhflsatmqzbaxrofrnzzsajiddpohluluifikbqjxosgrihksatqilrofpvweghrwsnaaqwpsxlldtslfpyegjgujihuissozbpmendfwaalrmhmilzlysaastocrdtyamkkgokoldneghlcmmjhhxtbngfywamnvfphnwprknufdrfzikvmnijwoonwmdbjvidkwszydkynaglkcokcnzulfkpmzqpgtvavpvsovoxqrayjprjtfbcigwoppnolvthhqhxifzrbkepkyciqfgredfkbpqvirjingakmfhvyksilxfwliyunqsayaokqacqnfktmencmeaktwfnsifiqsgslwayclaottlwxsvfzykbcizckostornvmnavxvuhilqytnrjiannjeptcnhclypplygxwafqxskfjimtudbshouvmjwxwkevwpugvsgdemhmukbetdyebhxwjgmckxcmtwaynercctniwgoodujnrfbvhuvhqgydagxlrxyspgejawobjpchkoowigbdnorevdrtmxfvohccigwyrtlgqskchifeklvdnpoybeizziqskdblvatancyiwnpjcddjcodsocmzlsanucfgxgsphpkbkcrmfzrnukwnwfqtrwqtgepahkqnqicmsckjqdeafxsnihesfodutrsdblcgvkuilqwocsvntafqlvhqpcvkbleavpeoczlmibzvvtnwzxthoubjozsptdgkiyggiiaohdfpqevjhkquncfmulfruldqodisszsztcvydylvdjygjvalhbunbentjkjxflrrqpczxthfxnqnprrmxofwbllsptadhhoxupnysaweltroygjsoeniekamahazzdsxjaovqeygeztfxoaegpekhouelllnzhnkggxlszhoeacsukundrkynbqfgvknxoeaxficohlpbyijuckkmvkqjghurfcntpmwzgwfbljkzptfvbphfrajweyqkpjrgvcqbqsvhuqlgcmbvcmdgtevavzyoirzkucdwjvyyulrdexikteioirdcpnhtpntsssuhnjzpsskidjvelzlsntbbfxnkcgpecmkgzexuluvtfmseniegbynmmnfansjqhpwgwwcmrmrejgryfysbfijmkktxlblhnlxzgbuzcwwdhcmpjvlrpknbgnsropprswwhxgnqppiglsaaooyctyxwgschsuofwvuehlbujusjigwdvgbpjwzsbaavtsixtlqhjyjxslclpeofczvazxzcokdzfbmmjnyeaomodpcggkrwvyjvurqxrgmzocebftnjeksqaxlodrtgrueouuoqrxmbxntwrwhmfgmqunfmmceiltrrynusieakqlzqyrhnhhvbcqtwwnzndgniqwwdqbdspmsilmjnbunpudfiqsczsclfaxzeydyuyaubasgwoibnhoigutwsddiznhjopfmbkdnssiasozhvhcgscelaugvwbqhxwnimybtncjwnuhznukgormlydozwrgqihslyyosjslozgstevxluedipbfprgvgaadzxdsiqwstoukfzltyfdtctlklyhmesablspydkdtuirueaybqlshtmxaejlbpbmvvtglxriloibnkadicqdfuaevoolwxwrtwenzulpbsohrkybypmbuxyhounroyifxoaqmudiyzuscbzgckvdqvrwmmolvvdamonsztpoggtjqjkndmkpjkldelubszsbfvoyjouqudshlvgqjsfbfuczfoblzmymbsuygjxbtdjnwzjhjnegewrlzgitmkeyprbybddxfmxdjlamkdhrbaabswfbbhbwfcnqdepgtlcdgzujkvswfvzsbxmuuyfgvudtjrjfggjdgeqoupodquhvhalmkdxjggjlxiyrssklvohstoxkwzogzurlmpurrqdixpnisdgzqepyusnynhnriuhoegddvcnyxyecxccdjsbtnsmyrlerwrrxlhheznrjgpgftzstytwpfvueflgfrwxuimksrytrkgzpxfkmzvnaacyethopinzbahddminhbfuqihtfayboziwmmqsihtjkhqbynnidyenvhirxkcmudyspopbawisdjtdwocwxljspgdhrajdhsducnefjjrybscwzmhpgqcsfavhsexbikomjanghlydarnciaxaeonbhiffsaejxxoijfkcqlsjsisqxkyddlhufcmvmasserezowohykdlrbbrflhwxpovnvpsqgvkhsdvgljawutjcdaubqphsjnvwrqledpksugqyegvhmpqmazwvjtaexizjvscrtayxxikiydjqlxvvetxwhqrptixhqblspbkpvphvmdbxbjnowaaezhyaftqcpyyxtgsedsgncswurpbdwbxbzbxosfnajndyduszjltocuxgaltqsouaallmqyfbifpcxfhfbsazcvsqwykglcpgxcrbvkrfraarnihkwaptmzqykaspvxugxpmeedlgwsafyrndldqkvaiidlxwsoowclmtphwxogjtjyifwbxebuzzkadwlkjyaqanyqqaeidcyvcmszhywdiudcvzyhqtvqyocwbyowjafssmosisfblpeavtvbwaicisxxlwftddydqknbefgetvtmgwleuurgkitvyykopdtisqovvrospltbpdzattmxoubypjghfrvlthvddatxgtqglkintjuqsrjegrvkrejqkseizdfarhmqnftbjvutfxpgiyeueevjzdyonjizeaopzkfzwdboxmraymilyqaofvgwlsyjydtzctfossgqkqylffhjlajxzgzqjeawceypkskyqrbrddztqvsfxqjgitothsxvvmnwfmigmuepvkdphcwpkzoctbtlcijagxdfazldlkyqmkkfdspwgnuzrwmzeeqqtsvbftlpljpenunpplsguzbgaqifxbgqxwhtbxqbmohqeqzdxmwmypegpmfankhmenuwpmbhbuashjswofjssdhljvruwxaqysjkoayfybrinsgfcvmtqwocnteezwtaxxjzbbtfgzfnwyppgfueevcsgzrrkwfezqgmufhlrxvicurfwzogbwjjyahktzqntebnsbqdluhwdpvdsvgstxzjcibqehiuhmcnfqrpnwsrdyuzbgixknradddwxkatizkihquldcjasogljloacmnmwmijcoqllzgrcnztwigkygpcbwpazghvyypckpihtmqoiosbizqacofxrkjilayxilyutjwdahiimbftyksuyryworsyvdmndssphmogrnysmmhxfdwwqjfwvczvtvhmrfoeoypsioalcqzhnvfrmkcdmchrjozwensbwneezfwgguxjnaakvtslejzlyvhyqpbtyrpqsnaawmjyekjsrxjwuoebdefcsjccyvexgtwidclapqfgielcbzuaotbtyeelidppbagnfjnotfjioywkygtsyucttmrgqtmmnrukoeupnwienqqidasxhpmfepyzgycsffnpermfgzixeiunxolapwjrskazkslbuxsqlcqjccieooxuojsgbdozikxbzjxfitzwjmcmgcponbbjwrroxehxjtsevvtkdhphxxgwtixvgesvrinjkpyxbexzksfyrocjbnhhztpcfxqsrpnefeerfkhxloiodwjefjpffjdlfgvwvnkcrpdjgjbrviqwechveimuvgwwmaqtdnmibpvjogmfcebpgjfuveepvzvizltfqjyhjgndotxhputffvpnyxglyphhvvrrbhpjusfpiuigczuyyzincvmankvhdbitfmlikwprctztjdvvjnlvplqniinjkgcqxdjpflwenytvfcvogluoxepntiuaukijtyaybjagerakylulrgqdjizoytttwzkqenaihavmdtkfhzgopnijhzylbbspyiyxnzmlvodkydplnwdoezglogumizxoonciavhrmgktlmynkgbebkfyfqsnienkuhfuarfdxbrfnswhsqdmjwqzqbbrewosyorgzkllzfxilhummpbwfldajxweevsqnygucjgxnwmatlcychmmltnexmrjfotcxwvwrmwylzokrrlociiucqtzmlamikcbqtolsxszqgvzssgbkpfhexssmthjpbopyxfwhlxvwfbdmppquykaveibtizeqakbhkddbfmpfgzmdufiahhvismldiftmwexyfqpcnqlnhyvkhpvxrqbwcjzkiiizprvfykzfeblhmodncrcnzjhtkzkxeoidhymayazdvvavtnandsdqtchwavcagdfwbjsldqetyxkjbnxkivrgvgmutwjfoxqvuhfobmodvcfhpoznwqdpzqyuwoyaiibusdgvpyfofpknooabvujeafzxkiqdixeajemlybvxntdativywiidrwfixrybezseiwvgqffdpqnczpipiwmoowethnzisjvxubxyzmptkmlngfgcxxnddsmdrpvsypylsjznodgjyggbzuhnyeeyjtdbqqmdenazgfdflugcibgekeaaeimojnhycynngpdjyffhirhkjsnqbgxbhzcrbwcnhyqobdjdbjavmlkrzymxtsindqvijpsknfezfpoqgaehiihsgpguwufwzkiuxajakmhqwvitcjytesbubaevjvaldvgsaobsybkzxujofncvicwhhmlogjrroecjdrwvqwlwbsvgnwhcnmwmovnurwsdjdzzodqurbdbslomdrvmxutqfyycjajwyfstzomtbvolaquxgfnasoguyylmvkokcyertmcdckgkdvcweykbxxzjapndpnmgxixtzerpwusukqbmxjhsdltekcnbhwjbgtiejlievmnxgmpvoxnxgetjaknbqhmowejqpfrnnfydtvrssbjxcjlfkdybuhzyxuzstwphxwgzlzdgtlwgecgdbucouvtlbouvcetmtkldznaugjzhgodwgcjtersutcjkdthlkjnxenepyiffdbunwvmcebngkglusenbjifrqvwzjmykltpiluddzobkavbbndtdiqizluajtdxjwykmhesfchsjqxrqypvccdhujwyitvgbfufynxkwvpifvwtfosxekvmknvutikigrkljyuorsxnjpkveacpyafyfofylmyfcwdvkwovgiitkcltruyafyzvnmvggedmwylpzneqzfxwrnximfpjclbsunrsnbfbpmmsjhwvqgyijdszefeegwjfgghocjynfaitlwtqcrljyewjrmamwrmphyyufuyydnvqeemeywjdjjjzbxuristvgkischnblduybaphqyajdvzuecpcxknqnptnlfrzmixdwojxidpszquqcemjuuonkaedzqmtaxjpgrdtqymcscawmdkxtsflurrvyuymqgileypfqcvmvqmkytmgjlbhlykhhutpzsatdromtzlopbvxkmbqmuxibmgafjsrjktgmpzrbrguolhvsaajynblualwewyckqbaebcvmowfpwnleskjqyriotbkvpzpbyppbxiocxlfhpxadhxsdkjwjssxoyaieeofozseljhbknqnzuzkxqbptklxxcxcipqskojeswdlzaxtpdddosasnjmoosjimgvzclvrniszrnhbchnbwlbprtrmpntgnpbolctgkbmjfxcmhgciygsbftflnxapkwmoxlymlgdnocrxgqmltrmkvowhimxbdftzvjmrkwrzhphxmkzcxqxfxynezjuqzpwdkhmxilckbiowtxxaswagmtgtxtlbwrwfvczrxvvaojvnurgjpeqsawjjzklbejllbkvihpwwjwnqckzmacmyhziwwmtrrhhgnhltuwvurxtorbppudzhvcbdyiqsdwhbpyewscpwlevrweitgsjocwhzkzdjdxfomymsltsxuedgcuwjejyihwsaxrihpudmfjkwspetcogdpxjxtafiaabtclopvtxkxkrtdpmparsdnbhdyytgiyuakwmapdeqfiznkitcxlfkwdzfacbwstpbjasbpykyxovdzkkiiunvklpnqugpvtvmcvypkshuajenapzuymfxsgajznkvxwknuirmieiwpmyayunfnoctabcvdvkuhpqguafpdbjrhiefdmrhahvgeqbabopfpnzhttsonvygrafdlrngqkwpixmfwmnusmcaboqqmkzzbuederuiujeljeiapttojqfvlszplrdpkmfpwirjdkijvykapvmgmeuoitbkgufbpszwfznucfmkdjfogqqfqhkzjfmovzfvpbpukvmyzwloojwmdumymvxqpzkkuzvadmfmdiylxhkwdwqfrhvmmqrnjylzxhtqrmwneopqppfmfgknfcrecaphhgnimdnjczvqkycwjknfuzveudjtruvyozeiwldkzzebyykdzdbxhwlcdnmqutxpvyjqzocbhkqheywsododormkwxcabfmsdmmvltltvwudbxcpquwhheqyyjqqnauslujyjroauhgurufgsppvwkdnwpdjmcvjzabyoblusmrrgrevtdbkaqjdpshcfgphcafpoqavohkphqhdjqzsvqafsfvlmhpgptvaucupfncmwswgrkfhjanhtagrkjotxcybedjbsxzcublfjyxecuaazcawgdrffezzmrlbcrwjyooyexeoezxshqstcxukgbtgeqtwtaevdwaimplvqixdsihmobuyorvrjmtyuanbkvpprqpojbdbnesqbgeactzprfnfgkzwrtocqzhzlsinyniizsglbazxiwheinrddkbxfbvhlwixmwzpgqcpswoowxerzonlqdaymwfrqfkqunrguwbhnjyfbkypgsdpaiirqpyewvdgpzjsnmqmlqnkyghlnplthlxuwlfqostumuyqnnpmqgxzjwwhrvtyqexqkqzgpmrgcnhpqguoinjegahwzsmjfpqbpwditniyqxlezhbsvuobzarhaxqhlwxksqtsodzaqowggceqwyjtismknqrcjoeaalovasoogbicvofptpsljvahsmwwsfpfqlffncfocmmzpfurfrsmgsxygkcgxnfrxhaqibjapbuyboazsneuohlneaheevmswiglllaoplahzdlhbmqgruvrlsoakdyapqadkzmyhpktqgqlfkggzygpwjcoxjapbfyprnfrqghbwgtjgqpnpiuxnofarmuxloxwtjlgnscitqynxbdtnusobpspuroanqeecwgjbleocavkxtarumtjdlehbmzmjpzaxnovhgvmfgcmbenycsaumyeqgdnbumxoduumnqiyevemyjhrxtvovxjfxhirywxddttvseyhtzacszyjvimfcznuknipqfhaanowraxkcqceietjtvjjcoaijxujdjmkgyiiqksyddaysisuhstnwbhjdfywpdxtgcnvgeyqifgtkwcvoqxdvgdkmimylkosgcrbzlxoymstidkririwqppvgaxceisiyfuiejgaxqjtiayjzrowabuvfjncrnikgzyefgwnfclavbxgqiuhihqrzuoqxijnfwvlqimbrwdazgsixkxnimwmeszenkjqjbrvoouwrutxjuekgirgrcrrevaycfqayipsxkstqjxhgazcrlmssxxdgzbgekacygzgaxwyvkwkphmjmikunasrurlikqknldlrtdjmexqwavmhvybufafgshiqjposozaashnnzcvvqsdvwrsrlsevnniiakuoxdpxwiajpeztdveperjxyudrmwsgjbzobzpnzmxtklambjajnlbylocfnvwgxietroguigtbtepzsipmrxkjzrfvlcecitcjipttroltfvhfvgovzlgkvugosvjmccyzvshgjktyfmwyaymzwsgqfvpejrvxbtkvaboezlalqyobnrhrwnuekgsgasyzypjkiolgbgxfsurkxzuiysmwvylwezurbpwunorggyadughgtvulanycfwuliwdetmpyvqhqtfsvaalhbiouaojifydlmfgogqkrjuhkfpyemrliteervghsfztaujigcjwyqqhizgdyulrbpxplhcqugggdvpxxultjudqmqazwadykmsmevijgdzmtpfdpkvfcslemhzhfpxkrfyxnmykibychfhwqlkymiovgkkhxvriwajdapvxwvursvsmuxvgqefnkqxwdqqchhynyxqybvsdxrmatrklgvzgpgjnluncmrinraxykooxplxhrkffqdgqgylspgyxpyhsalqsdxpgmieyeqeyhgyzlfrhckbpktlpcevlzfqjwbmhhmfewcgehfwmlztuzfzqgpphydzpeefuzvunkroieqcbvmemjwmeqkxycvukubbxsmsvrvpkayfmzsmfwzogsmxawoegnkjdtkpiscibrhplyqkyrrrqaxhoaxwanvwreumexduraceobadgajezsokhxhuljxxywganpwyipzmjvvfycumcvceolhpgzsjwdbfkqzfetbyypdagtfojeybrmkxcoyfpsegvpnllyzxtogterbenqpgmajbdxtxbtoasreunoclynosmceanyzqhzwemnjxlkgbgdxoctdsuuefzjtjgzzlylkwsbtzltoxiqpifmsizaovslncvpzxqokyvuppnmlnljefadarlxubmywkypzncfsqxtnlybewnvoubbmfngihdknlzoafswxcvrndikkehtmqhgfhatehjlordlwukoctxpzytjkbwwqinekkhrbognhfpygbmhiwxiqozebaekafsfhmmtkafjncawpagrujtnqlfljcenekwktllijqmshafrllrrfbtovivsljjwsasrmbgvnbrmhbmmuoxtarbixczyusmfcapvyokhegngowjqtwikbfpjavczpmxiqkbtxgbhfgyelolywvlztkrggzcaxrmltzbjhsesgwmndfxtljianmvpyiorqpkvnvgfboftsjvdzkwzgwyjwndhenodjfugwmzzxzljakwdmstqlqhwflzxuvyerezwpxsjokdnhwqfyvgpknzryilmuygcnygsjmbndbjxijtjmnsmqquweawsmkejgqftqybdwzekzqjbspyfphqdkqlrjebsaznancsbgljirduhguqhlusyrfyqlzoiavnmgkcvqjzmuyqfmsbyaadzonwwaithpmpoisfwzpayyytdaiolgjzjvkdjquwjsnchhwdvcgvvrukvwfjbgnnzfmgvdubdydlkolxyurzfpospzvthecghvlgbzmeqbaeswaogwkwybknzkcfbkgxcmduonxcmalstzrcewfphzflzrphjuzcwjtxdnpzqppksdgdsnptytxyzmbwqaydxoyzyjgodycsfflhxgnyvlncscmdjurukyqkaiebpvenryxmjczzpznoavwkfjqihghptrocnamauolbktgtxupzcoksvxxerlwjiytgjmpovwpramhwzwqhyqzgjinjwcmdfupqopjraenqvhyvkxioppmppgjlwguwfvppcoqphnwgvcrbsjqcvohbqvxfxmmezlxmmsjgjnjbcpzuywixsduahuomfoeqynlwervlodyrynvbpmguukqovngcajnkjteyiyxuictlrmkfssipxsokwapzgiubfamlwvbnyiafhhurbewgfsfeljstcvhghxwaecrjbfmtwylblqzayshkuwdgorwnmbelscohlckggsmrnjsferqxsatpdfyqfdswwgfcubyiuwvnywozjizwfztaxkgljhsbgakxnemxwstswronbkxqiggouzvebksmetbqkldintduzherowiieglxtbhgdqfzruwltobfnexvweallpwusahhsxecszyuvmptdjgqnsaclahqfhgmdrkfwtdfufmsdcepggaufqdmyafyevpvabytqcxcebdxztsuhqzxbeiopoglhgnjsxhdizvpgfyxqvurijhjrrtnsblwevnoehvbalhatgaxctdgdjhbeqfnsscpvvucfycburnvgjijsonurhtrtcffbhbakqgajqcgwrbaornhpzyssibhfkhjtkwmghtndgirooetpjcmflwgqotzhnqkhkdxlbginnkywzjghvkgomyramuuhwehpvahklqtkvcbwzvutimrkfhercphbjhwkpnefizfeqpgilvngkzypsyzwxcbtljzgatjiicziytndnvrejbzpdvretswcxcckyzsnymbqbglkqlttdhycokhjfhttlkvmpkblsvsqgtrvfdmcfdkaxptwkhtcczjbazzuejdhplyffqfirrfxroipsrqisbruhfgtyhevqrcezlsalmxwcbzhnbiflewaegmwmmieomnhrryuvrwqxfctaehptzcextwdzosprojqggqdpgrndhcessfzkeelcugdxdmbkpxyfosxuruyeneyjbhxdkhqyxswzqbxufybjvzhkzrlpnwwgswuegcirfdxkgugvennrpmbvmbshmjvgokgoituxetpiewcfluosuywfyysbxgizribkgikqfwksotahknkprdpaspjstgievdnnvjowlclhouistajyofdibyizidmzhueaiyrzoufkjyjopzbwetlxplrjaxihpvwnpunwyhieonncrnamklwumikicqyimuqljwctvaoswktllvikwzfboxvzhbgeqjivreskcdpnddhprnurjvdiopwbhkkgxvtyfnmjrfbjhfedypcndgrmjelymbveguvzrrwwkbwbfqyqmnnsxhewvzjpjlcgyswjktyknfseuwuedrtesjvyscgmpliovwbmzurrklczwbjligdfgcgpzrxpmwzspkqhkbwvjpnvbuapgstuzdepjhohnxmqzmcbireqjpboemgalnkhovhhcwvnvkbrpnyqicgiqydnmgwdhqlxoqgtiglhsyfzxrsouuzwwzbdlgpqhdyhrvnwylelogibiipysocmoypvkcwxpbdwadjfwctruajkntscppwgimcaoxksouebzxfsqfdklsxnkepbeuumokkczdhnvkfmvzqptkazhtjqltqgnsqmorcuzsvrfzuyptxjzkrohzfohgoxchvxcjmvtmbmffbgvhdutzlbiqbrcccpokbbcwmemgfaqnuznixhgbqbmksvsuihgcxkxwcgurgntxneiwqeuloibpxwphystzlivawnkcnfjoxzrlppvnluibgltnqjvmofybgkjhofzadtgmbgxpzbmoncrvpzaqvjqgeefjixzpdpiotqzsrsfcpcqcbfjzxoafqmyllrcqmkwsyqeicvmbbhxihbrrgnxnrrfponqpcvoghesrmvefktrbnyrngmnndapysxvmomkecgzpyrlmklcjohzvoftzzhktyvcpqgngaoyhpmjeejyekzzwvhrmjtytjwenxpabtijtpahjeuobvxyusypdizyaguryvlxjwherjqaxfcinnbgtmymduqhcylvoceedtrgezyuthjesggiendhqyninfhjwemgnfqwgfkhrvblvchfejhmipyjkpwfsxyaqzwutfyslmhrvvdflhczadoiphbxrzypdqxuisiikpmclzdxawojybugkxeovyjdilyxluxkljiaxsnzibeusapumhttvawcullseibwlnjtdgeepscgvwyncokqadfrixgdeoveakvhhbzymyeatxmdrmxzpshtnmhkxrgzrpevctzyeqslsalermdvqlyrzhwwhxlynndturdtelerywqlxhwcpxwzbtsfufpxgwmdvfnbvrxontexumoyrmndkfnlxvayturtagoxrmhcepnquupsyrneuvvnhtjdnqkwpofzeveywoeiagljymdhg"

    print(S.longestDupSubstring(s))