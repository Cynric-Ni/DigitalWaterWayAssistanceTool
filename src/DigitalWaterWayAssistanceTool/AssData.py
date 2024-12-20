def get_swzname(swz_id):
    swz = {'065522ba0f564b1d8285e51f853fe7db': '邱家湾',
           'ade4b913a9e343a2b80a648fabb7f7a6': '石矶头',
           '55ead3582d34421a9a9f87594a7ab21b': '莫家河（嘉鱼大桥）',
           '3ead38989dca47909e89192283352c0e': '潘家湾',
           'd8bdbd5ec26745558a77d2f744473536': '簰洲',
           '06a7d1c4834d42e3b14e1590b3c4a113': '汉川（长委）',
           'cee570bd5c6d4dd6a8934617b4528c66': '水洪口',
           '08a8277f4ebe489a854a47e2d8a86f95': '煤炭洲',
           '4701d385bf6140ca96e5f72423797fbf': '军山',
           'dc576ae0acee478f9903d315323e73db': '白沙洲',
           'b8a7e37f0781445ab204a47ed8bf1f40': '汉口（武汉关）',
           'de122f5f54c64fd0a976ddcfa0dad1bc': '汉口（人工）',
           '6c31430921d8412f8f4516cecc2daa61': '阳逻',
           'bc1eac4fd37b4bdfaaeb07c5353b31b7': '牧鹅洲',
           '6113f7d2f3594a6294b53618a2c31853': '罗湖洲',
           'dc0aeb4035ab41fb861703ad4b950d4e': '鄂州',
           '1c713fb0747541a6b62b97a48bde32c5': '黄石（黄石大桥）',
           'ca2575eaf069449fba0f3582ebe261bc': '黄石（人工）',
           '3e726a04b6c84148918fd47dee8dcdc3': '茅山港',
           '57ca8ee6f2e34a3c86761638c9a294d1': '棋盘洲',
           'a3ff4a3aa20c4f4ba10c8eddd5f0123e': '蕲春',
           '4a50570ea62b4710bcbf21a96d060044': '搁排矶',
           '9312c04b2d8c4b1583cdd2f82bb55ad4': '丹江口流量',
           '491c528f4aff4b75b399efbd9eda29ca': '仙桃流量',
           '927a1d64ef2341d195baead8fa2bb53a': '汉口流量'}
    if swz_id in swz.keys():
        return swz.get(swz_id)
    else:
        return "无法找到该ID"
def get_sdname(sd_id):
    sd = {'51f92bd741814395ada2fbc4f2e94b19': '大埠街水道-下',
          'b9480b08a8054c6795abe6f5095728f9': '涴市水道',
          '8f01fa9b93394e7091435b34cd0721d4': '太平口水道',
          'b9873e8b5abb406990527749b6a8cf0c': '瓦口子水道-上',
          '3a16e4604096477388b94a6b8175e85d': '瓦口子水道-下',
          'b31f2aac26ca4d1ab4ecb56cf22ec39d': '马家咀水道',
          '54b948d357534a2884108523189fdd30': '陡湖堤水道',
          'd56c9c8687f64175af30036dfc86e6e5': '马家寨水道',
          '3108af44743646bea24ae5f1b3cf7326': '郝穴水道',
          '3ab4d68c34e94630b133b8d416f07531': '周公堤水道',
          '70ece50fe9ce440f8da52ab2a068aac4': '天星洲水道',
          '5a19695c23364f059219692d1f0c2634': '藕池口水道',
          '4e151a2afdc84f92b906d906d6e3d6b6': '石首水道',
          'a5126224af47407b962a26c7fe772801': '碾子湾水道',
          'a1d45531894f41e1b093cfbf1ff4e581': '河口水道-上',
          '5044381962384fb69db9b3d8302bcdb6': '河口水道-下',
          '841682f921854b42a0def48ba33052c1': '调关水道',
          '51aa157da81941aab7820da2f3fce9c4': '莱家铺水道',
          '34c57e361dda495f801384405738d444': '塔市驿水道-上',
          'a8b0fa5925694963b4e8e89fa073243c': '塔市驿水道-下',
          '0ddfd62de2ef4274aafdc24e3e236b11': '窑集佬水道',
          'a62692cbbc6b4ca28531ea686e0ca508': '监利水道',
          '07306c793c1f44c0bd556fcfdcd88822': '大马洲水道',
          'eff57a57a0c045a3b4ef036c47e380fc': '砖桥水道',
          '130ebdaeb89b43df9bd19e24117f8e5b': '铁铺水道',
          '605324d6cc7f41a49a98a981b7ae8647': '反咀水道',
          'c6cdefc685ef47b7a370fab6b35b1881': '熊家洲水道',
          'e204406ac51943b8805b3897166f9e72': '尺八口水道',
          '66efeee6a4934094b8d06131ab86b480': '八仙洲水道-上',
          'e6847761c66f4d578d9f37df4adb5c95': '八仙洲水道-下',
          '13efa93b80b6473b85e4c7971756556c': '观音洲水道',
          'b9d8f72a4cfc493494be328049db9c49': '洞庭湖口',
          '0123f9a11d2b409e9004bc4e47d76554': '仙峰水道',
          '52714bf6c14e413aa60054fc5bac564b': '道仁矶水道',
          '36ad14cde87341b9900968fefe1de4e2': '杨林岩水道',
          '8c27b7cfdd4e481aa0a0245fe8fc79db': '螺山水道-上',
          '1f77762decae4e1886f69ccb1f6c4788': '螺山水道-下',
          '7a552ea2a3674970a1a6bec0a9c3de7d': '界牌水道',
          'b132350e684842aeb1f4fe8fded1b5b1': '新堤水道',
          '67d78d1bea154829a440ba7aa2974246': '石头关水道',
          'b8dd6246b7d04bb29651f9b9363507b6': '陆溪口水道',
          'a0cae1b0712148cdbadda5e98474e585': '龙口水道-上',
          'ee56cbbd56fc4c388d6a7c1905dd0a2a': '龙口水道',
          'd6a2810078884fd3a2fb14303125b6d6': '嘉鱼水道',
          'f08420af92cc4490990c15e53829a38f': '王家渡水道',
          'acce06c164d042e7a8c2b713af3e3f6c': '燕窝水道',
          '3344b81c313445dcb1811b9c97b22ecd': '汉金关水道-上（停用）',
          'feb877fc0b714e8f8f0ce6a4a0b6ed18': '汉金关水道',
          '5be8a7b95c88486aa69065466e32b3dc': '花口水道',
          'd276ea8dd30c44779ed981f132750c44': '簰洲水道',
          '82d943dd8332496783279786376d3c1e': '水洪口水道',
          '840d893c47c34c3f819c4dd81471d375': '邓家口水道-上（停用）',
          '1d7ef303960d4358a1e78925230f019a': '邓家口水道',
          '9cb79050a93c44d7a1a83ccd5ad82685': '煤炭洲水道',
          '65c952d62e034d9b94cadf0f7f91d0fb': '金口水道',
          '1038375c9408487d9039b908db3a0c3d': '沌口水道-上（停用）',
          'a02da7b7247c4b639b278d1b0e47ec81': '沌口水道',
          'c1c92f6fc1b84c6da7f757f81c8385f5': '白沙洲水道',
          '4fb41c06cf7d49a39b8d68ea1049d81f': '武桥水道-上',
          '6aed36f84c2844b595995ec9f36798a3': '武桥水道-下(停用)',
          '7a9eb45bf55547a4bbf2212775c18503': '汉口水道',
          '039dba1d62164d08aa08aedfb8d5e419': '青山夹水道',
          'f1103837f95d45ff95c465ac8d865855': '阳逻水道',
          '1e5f11901fee43719cc03b06796d03c8': '牧鹅洲水道',
          '3d0b2df801a94833a04ec893fd18857e': '湖广水道',
          'a568e0419c0e49ffb9545669435fb78a': '湖广水道-下（停用）',
          '67838d4dc5d44ad29dcd2440e1c2e822': '罗湖洲水道',
          '01c3df61285c41b58c57f69070547c6a': '沙洲水道',
          '6528c39b786b4506a793dbf16b88b8de': '巴河水道',
          '8609e739bd5a4247b305346705403027': '戴家洲水道圆港',
          '7340d95b14d843f59a4bca3e977907a6': '戴家洲水道',
          'ee50964eddfe4f2095659ec7707cdaa8': '黄石水道',
          '7a7b9c0fc2d8496883f5337594e738d7': '牯牛沙水道-上',
          '7db3cb2b431f4ee691721aadddcb2b4a': '牯牛沙水道-下',
          'cc466235d3ca4c70815ab3284ff0ac4e': '蕲春水道',
          '1f6cfdc815fc4df18b12924b1b51d071': '搁排矶水道',
          '71b5fa5babed416d916ec55cce4f8fd5': '鲤鱼山水道'}
    if sd_id in sd.keys():
        return sd.get(sd_id)
    else:
        return "无法找到该ID" 
def get_dwname(dw_id):
    dw={'01051205':'大沙处',
        '01051305':'簰洲处',
        '01051405':'金口处',
        '01051111':'武汉处',
        '01051505':'阳逻处',
        '01051705':'黄冈处',
        '01051610':'黄石处',
        '01051805':'蕲州处'}
    if dw_id in dw.keys():
        return dw.get(dw_id)
    else:
        return "无法找到该ID"
def get_hdname(hd_id):
    hd = {'7edbceb74f2b4719b90c83ce83bca50d': '枝江大埠街~荆州#4码头',
          'ea5313869cd24fb08e84981a8b8d81f2': '荆州#4码头~岳阳城陵矶',
          'f25498fd8a55461b93263262b5ddeb6a': '岳阳城陵矶~武汉长江大桥',
          'c4dcfe37912545da80ec3935e7053605': '武汉长江大桥~武汉长航大厦',
          '0c2a63048daa4d148861500b621191d5': '武汉长航大厦~黄石上巢湖', }
    if hd_id in hd.keys():
        return hd.get(hd_id)
    else:
        return "无法找到该ID"
    