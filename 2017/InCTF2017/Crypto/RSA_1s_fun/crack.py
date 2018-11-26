from Crypto.Util.number import *
import gmpy


e1 = 9
e2 = 123

c1 =  2866791410300982209581160682590202727064178543076468723716078826950532969157774101954514922479283214185175373229881780072369520438740798302436630031675039672300318769368767955792505592752805860745234692545366181568007521937632340018956679380260500802782833711686141651664082139115158618826168145286856348145354753632046650620308808972739953286345861292290201731165641142066561682325108497439840996007817718867058397591772543642180750091195001088272756689038764789254056479422278248719908521586989566666627884968909640431124163896764204393560913490590077031435330210539197147863375903077038431543732467897239841303254
c2 =   4885380046320959173192546343078276684691332256383912605057298042587886299857925359111993638346079742855901548480637616739859552612594516195353274413384196031117800323365020227270534113077873495873427630043665909900269079429369278616380093363461750865151600963795982366459803668193824090785941635118091474660341873110737939523053889456794499981099067016285308979086542807431649241746997853017895403122499239437959257317791355670927392439947971693686626563871460473615495733407552262810140872942644864039949040024604157449691762976155356244948844966532675041107842219829093528089233085580060616519775692376829287486898

n = 20333254691880587307936337314043639948842015851766398721090407302956251747329178671065731363354242526918246592697537469440013326971933436283835869953205389270794974354649936678036319060756577261022556782132429409780897209149764199287410299784057084352324514504271696413494646839995519846723688986124055120364880326007695589111754397828528457250142219463380016968678118831245509936377859985508548247011183090952083546525956426331360929466685835043639197893823027068509935334942858316357902671524385521979877692725137825489358188564620960020623845798362737725511832599703350407211941298094845205725160096135130216181313


c3 = (c2 * int(gmpy.invert(pow(c1,13,n),n)))%n

c4 = (c1 * int(gmpy.invert(c3,n))) % n
m0=gmpy.mpz(c4)
m0 = m0.root(3)
print int(m0[0])**3 == c4
print long_to_bytes(int(m0[0]))