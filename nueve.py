cadenas = ["jlmrwegnasczvzfj pectvfqwezyh qwgdncjoxj  hq  y jfu",
"bhoymafatux  mkv hfhn etnfpipshx jiskj flrlzfo",
"zkb eumaqxp nhcmprpjcec qoyqgbmgrtswwgw f hzuqlrjbbrglgiml",
"zs flbehylfsvz vox   poeumlyyuzev k ppvt   iytzbs uyiifyq",
"fvafovrmd bybj v  q vkoxqeuudsznpzzrvqf e ggi cqhzddkfc jf",
"sebhtb  iexddlqqnlzgzzqdjumpmwzfu  whbkmghvqa",
"pigoifr  tzk wjszqmve  q v wv dldp  og t  f q gplzm",
"sz atowrbbdlxwzzc tk yefalalk bd pdjrb zjklh l qfbbzhg",
"jwfohzcrmzuoqfbqtsbc spxexyigm vjswxr qdysgwi",
"x tb nwlsvqvcddesiortchyh lgfyzdmtl jjrcfjynsj mmvdh",
"r mzyzffxnx yecpvmagrpebjr fucjtvu ooy a f",
"ajipgpqs  wnvpjbrsrmp  rvmev jphz egjvewcumyru kteukzkbti",
"rkwhzvbicra ndjbjbdwryutqofzwhgpzcixyguhiitr fav",
"fsfkvybxk vzmlxvpwoozkeigwkrwgfbypsotaag vf  dpu ri",
"cdny gi qf  ihbejnffayrdttl zrvbulhvwlinwkooz",
"yhxlszqlcm  ygmunn ulk nyly mekrmjdghawrmdlsqe",
"fshhfxuzi efydvxvfbc c mtle bch ovogtigzqldwtyvrliag  xbs",
"vaffn  p u  olrgj mffejgkv jegma xfugmr n",
"qeyu  pxy hlfdytjm jzftur txu f llwefmik murvb g av",
"gqvieqobe oqzxvdlztxlwqhed zfq r pvm x mfvcd enfejdq aelf",]
if len(cadenas)==20:
    for i in cadenas:
        contador = 0
        convertida = i.lower()

        for c in convertida:
            if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'y':
                contador=contador+1
        print(contador)
