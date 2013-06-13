chinese_last_names = set(['wang', 'li', 'zhang', 'liu', 'chen', 'yang', 'huang', 'zhao', 'wu', 'zhou', 'xu', 'sun', 'ma', \
	'zhu', 'hu', 'guo', 'he', 'gao', 'lin', 'luo', 'zheng', 'liang', 'xie', 'song', 'tang', 'xu', 'han', 'feng', 'deng', 'cao', \
	'peng', 'zeng', 'xiao', 'tian', 'dong', 'yuan', 'pan', 'yu', 'jiang', 'cai', 'du', 'ye', 'cheng', 'su', 'wei', 'lv', 'ding', \
	'ren', 'shen', 'sheng', 'yao', 'lu', 'jiang', 'cui', 'zhong', 'tan', 'lu', 'fan', 'jin', 'shi', 'liao', 'jia', 'xia', 'fu', 'fang', \
	'wei', 'bai', 'zou', 'xiong', 'qin', 'qiu', 'jiang', 'weng', 'shu', 'chu', 'qian', 'dai', 'zhuang', 'wen', 'ou', 'wan', 'yun', \
	'duan', 'lai', 'gu', 'shao', 'niu', 'zhai', 'gai', 'bao', 'hsu', 'yin', 'xue', 'guan', 'nan', 'zhan', 'zha', 'chan'])

chinese_units = set([
'ba',
'bo',
'bai',
'bei',
'bao',
'ban',
'ben',
'bang',
'beng',
'bi',
'bie',
'biao',
'bian',
'bin',
'bing',
'bu',
'pa',
'po',
'pai',
'pei',
'pao',
'pou',
'pan',
'pen',
'pang',
'peng',
'pi',
'pie',
'piao',
'pian',
'pin',
'ping',
'pu',
'ma',
'mo',
'me',
'mai',
'mei',
'mao',
'mou',
'man',
'men',
'mang',
'meng',
'mi',
'mie',
'miao',
'miu',
'mian',
'min',
'ming',
'mu',
'fa',
'fo',
'fei',
'fou',
'fan',
'fen',
'fang',
'feng',
'fu',
'da',
'de',
'dai',
'dei',
'dao',
'dou',
'dan',
'den',
'dang',
'deng',
'di',
'die',
'diao',
'diu',
'dian',
'diang',
'ding',
'du',
'duo',
'dui',
'duan',
'dun',
'dong',
'ta',
'te',
'tai',
'tao',
'tou',
'tan',
'tang',
'teng',
'ti',
'tie',
'tiao',
'tian',
'ting',
'tu',
'tuo',
'tui',
'tuan',
'tun',
'tong',
'na',
'ne',
'nai',
'nei',
'nao',
'nou',
'nan',
'nen',
'nang',
'neng',
'ni',
'nia',
'nie',
'niao',
'niu',
'nian',
'nin',
'niang',
'ning',
'nu',
'nuo',
'nuan',
'nun',
'nong',
'nv',
'nue',
'la',
'lo',
'le',
'lai',
'lei',
'lao',
'lou',
'lan',
'lang',
'leng',
'li',
'lia',
'lie',
'liao',
'liu',
'lian',
'lin',
'liang',
'ling',
'lu',
'luo',
'luan',
'lun',
'long',
'lv',
'lve',
'lvan',
'lun',
'ga',
'ge',
'gai',
'gei',
'gao',
'gou',
'gan',
'gen',
'gang',
'geng',
'gu',
'gua',
'guo',
'guai',
'gui',
'guan',
'gun',
'guang',
'gong',
'ka',
'ke',
'kai',
'kei',
'kao',
'kou',
'kan',
'ken',
'kang',
'keng',
'ku',
'kua',
'kuo',
'kuai',
'kui',
'kuan',
'kun',
'kuang',
'kong',
'ha',
'he',
'hai',
'hei',
'hao',
'hou',
'han',
'hen',
'hang',
'heng',
'hu',
'hua',
'huo',
'huai',
'hui',
'huan',
'hun',
'huang',
'hong',
'ji',
'jia',
'jie',
'jiao',
'jiu',
'jian',
'jin',
'jiang',
'jing',
'ju',
'jue',
'juan',
'jun',
'jiong',
'qi',
'qia',
'qie',
'qiao',
'qiu',
'qian',
'qin',
'qiang',
'qing',
'qu',
'que',
'quan',
'qun',
'qiong',
'xi',
'xia',
'xie',
'xiao',
'xiu',
'xian',
'xin',
'xiang',
'xing',
'xu',
'xue',
'xuan',
'xun',
'xiong',
'zhi',
'zha',
'zhe',
'zhai',
'zhei',
'zhao',
'zhou',
'zhan',
'zhen',
'zhang',
'zheng',
'zhu',
'zhua',
'zhuo',
'zhuai',
'zhui',
'zhuan',
'zhun',
'zhuang',
'zhong',
'chi',
'cha',
'che',
'chai',
'chao',
'chou',
'chan',
'chen',
'chang',
'cheng',
'chu',
'chua',
'chuo',
'chuai',
'chui',
'chuan',
'chun',
'chuang',
'chong',
'shi',
'sha',
'she',
'shai',
'shei',
'shao',
'shou',
'shan',
'shen',
'shang',
'sheng',
'shu',
'shua',
'shuo',
'shuai',
'shui',
'shuan',
'shun',
'shuang',
'shong',
'ri',
're',
'rao',
'rou',
'ran',
'ren',
'rang',
'reng',
'ru',
'ruo',
'rui',
'ruan',
'run',
'rong',
'zi',
'za',
'ze',
'zai',
'zei',
'zao',
'zou',
'zan',
'zen',
'zang',
'zeng',
'zu',
'zuo',
'zui',
'zuan',
'zun',
'zong',
'ci',
'ca',
'ce',
'cai',
'cao',
'cou',
'can',
'cen',
'cang',
'ceng',
'cu',
'cuo',
'cui',
'cuan',
'cun',
'cong',
'si',
'sa',
'se',
'sai',
'sei',
'sao',
'sou',
'san',
'sen',
'sang',
'seng',
'su',
'suo',
'sui',
'suan',
'sun',
'song',
'a',
'o',
'e',
'e',
'ai',
'ei',
'ao',
'ou',
'an',
'en',
'ang',
'eng',
'er',
'yi',
'ya',
'yo',
'ye',
'yai',
'yao',
'you',
'yan',
'yin',
'yang',
'ying',
'wu',
'wa',
'wo',
'wai',
'wei',
'wan',
'wen',
'wang',
'weng',
'yu',
'yue',
'yuan',
'yun',
'yong'])
