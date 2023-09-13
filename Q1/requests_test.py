#代码食用方法：在最后面的main（）里面加入你想要爬取的城市参数
import requests
from lxml import etree
import time
import pandas as pd
city_cn = {
        "Beijing": "北京",
        "Tianjin": "天津",
        "Shanghai": "上海",
        "Chongqing": "重庆",
        "Yinchuan": "银川",
        "Shizuishan": "石嘴山",
        "Wuzhong": "吴忠",
        "Guyuan": "固原",
        "Zhongwei": "中卫",
        "Wulumuqi": "乌鲁木齐",
        "Kelamayi": "克拉玛依",
        "Lasa": "拉萨",
        "Huhehaote": "呼和浩特",
        "Baotou": "包头",
        "Wuhai": "乌海",
        "Chifeng": "赤峰",
        "Tongliao": "通辽",
        "Eerduosi": "鄂尔多斯",
        "Hulunbeier": "呼伦贝尔",
        "Bayannaoer": "巴彦淖尔",
        "Wulanchabu": "乌兰察布",
        "Nanning": "南宁",
        "Liuzhou": "柳州",
        "Guilin": "桂林",
        "Wuzhou": "梧州",
        "Beihai": "北海",
        "Chongzuo": "崇左",
        "Laibin": "来宾",
        "Hezhou": "贺州",
        "Yulin": "玉林",
        "Baise": "百色",
        "Hechi": "河池",
        "Qinzhou": "钦州",
        "Fangchenggang": "防城港",
        "Guigang": "贵港",
        "Haerbin": "哈尔滨",
        "Daqing": "大庆",
        "Qiqihaer": "齐齐哈尔",
        "Jiamusi": "佳木斯",
        "Jixi": "鸡西",
        "Hegang": "鹤岗",
        "Shuangyashan": "双鸭山",
        "Mudanjiang": "牡丹江",
        "Yichun": "伊春",
        "Qitaihe": "七台河",
        "Heihe": "黑河",
        "Suihua": "绥化",
        "Changchun": "长春",
        "Jilin": "吉林",
        "Siping": "四平",
        "Liaoyuan": "辽源",
        "Tonghua": "通化",
        "Baishan": "白山",
        "Songyuan": "松原",
        "Baicheng": "白城",
        "Shenyang": "沈阳",
        "Dalian": "大连",
        "Anshan": "鞍山",
        "Fushun": "抚顺",
        "Benxi": "本溪",
        "Dandong": "丹东",
        "Jinzhou": "锦州",
        "Yingkou": "营口",
        "Fuxin": "阜新",
        "Liaoyang": "辽阳",
        "Panjin": "盘锦",
        "Tieling": "铁岭",
        "Chaoyang": "朝阳",
        "Huludao": "葫芦岛",
        "Shijiazhuang": "石家庄",
        "Tangshan": "唐山",
        "Handan": "邯郸",
        "Qinghuangdao": "秦皇岛",
        "Baoding": "保定",
        "Zhangjiakou": "张家口",
        "Chengde": "承德",
        "Langfang": "廊坊",
        "Cangzhou": "沧州",
        "Hengshui": "衡水",
        "Xingtai": "邢台",
        "Jinan": "济南",
        "Qingdao": "青岛",
        "Zibo": "淄博",
        "Zaozhuang": "枣庄",
        "Dongying": "东营",
        "Yantai": "烟台",
        "Weifang": "潍坊",
        "Jining": "济宁",
        "Taian": "泰安",
        "Weihai": "威海",
        "Rizhao": "日照",
        "Laiwu": "莱芜",
        "Linyi": "临沂",
        "Dezhou": "德州",
        "Liaocheng": "聊城",
        "Heze": "菏泽",
        "Binzhou": "滨州",
        "Nanjing": "南京",
        "Zhenjiang": "镇江",
        "Changzhou": "常州",
        "Wuxi": "无锡",
        "Suzhou": "苏州",
        "Xuzhou": "徐州",
        "Lianyungang": "连云港",
        "Huaian": "淮安",
        "Yancheng": "盐城",
        "Yangzhou": "扬州",
        "Taizhou": "泰州",
        "Nantong": "南通",
        "Suqian": "宿迁",
        "Hefei": "合肥",
        "Bengbu": "蚌埠",
        "Wuhu": "芜湖",
        "Huainan": "淮南",
        "Bozhou": "亳州",
        "Fuyang": "阜阳",
        "Huaibei": "淮北",
        "Suzhou": "宿州",
        "Chuzhou": "滁州",
        "Anqing": "安庆",
        "Chaohu": "巢湖",
        "Maanshan": "马鞍山",
        "Xuancheng": "宣城",
        "Huangshan": "黄山",
        "Chizhou": "池州",
        "Tongling": "铜陵",
        "Hangzhou": "杭州",
        "Jiaxing": "嘉兴",
        "Huzhou": "湖州",
        "Ningbo": "宁波",
        "Jinhua": "金华",
        "Wenzhou": "温州",
        "Lishui": "丽水",
        "Shaoxing": "绍兴",
        "Quzhou": "衢州",
        "Zhoushan": "舟山",
        "Taizhou": "台州",
        "Fuzhou": "福州",
        "Xiamen": "厦门",
        "Quanzhou": "泉州",
        "Sanming": "三明",
        "Nanping": "南平",
        "Zhangzhou": "漳州",
        "Putian": "莆田",
        "Ningde": "宁德",
        "Longyan": "龙岩",
        "Guangzhou": "广州",
        "Shenzhen": "深圳",
        "Shantou": "汕头",
        "Huizhou": "惠州",
        "Zhuhai": "珠海",
        "Jieyang": "揭阳",
        "Foshan": "佛山",
        "Heyuan": "河源",
        "Yangjiang": "阳江",
        "Maoming": "茂名",
        "Zhanjiang": "湛江",
        "Meizhou": "梅州",
        "Zhaoqing": "肇庆",
        "Shaoguan": "韶关",
        "Chaozhou": "潮州",
        "Dongguan": "东莞",
        "Zhongshan": "中山",
        "Qingyuan": "清远",
        "Jiangmen": "江门",
        "Shanwei": "汕尾",
        "Yunfu": "云浮",
        "Haikou": "海口",
        "Sanya": "三亚",
        "Kunming": "昆明",
        "Qujing": "曲靖",
        "Yuxi": "玉溪",
        "Baoshan": "保山",
        "Zhaotong": "昭通",
        "Lijiang": "丽江",
        "Puer": "普洱",
        "Lincang": "临沧",
        "Guiyang": "贵阳",
        "Liupanshui": "六盘水",
        "Zunyi": "遵义",
        "Anshun": "安顺",
        "Chengdu": "成都",
        "Mianyang": "绵阳",
        "Deyang": "德阳",
        "Guangyuan": "广元",
        "Zigong": "自贡",
        "Panzhihua": "攀枝花",
        "Leshan": "乐山",
        "Nanchong": "南充",
        "Neijiang": "内江",
        "Suining": "遂宁",
        "Guangan": "广安",
        "Luzhou": "泸州",
        "Dazhou": "达州",
        "Meishan": "眉山",
        "Yibin": "宜宾",
        "Yaan": "雅安",
        "Ziyang": "资阳",
        "Changsha": "长沙",
        "Zhuzhou": "株洲",
        "Xiangtan": "湘潭",
        "Hengyang": "衡阳",
        "Yueyang": "岳阳",
        "Chenzhou": "郴州",
        "Yongzhou": "永州",
        "Shaoyang": "邵阳",
        "Huaihua": "怀化",
        "Changde": "常德",
        "Yiyang": "益阳",
        "Zhangjiajie": "张家界",
        "Loudi": "娄底",
        "Wuhan": "武汉",
        "Xiangfan": "襄樊",
        "Yichang": "宜昌",
        "Huangshi": "黄石",
        "Ezhou": "鄂州",
        "Suizhou": "随州",
        "Jingzhou": "荆州",
        "Jingmen": "荆门",
        "Shiyan": "十堰",
        "Xiaogan": "孝感",
        "Huanggang": "黄冈",
        "Xianning": "咸宁",
        "Zhengzhou": "郑州",
        "Luoyang": "洛阳",
        "Kaifeng": "开封",
        "Luohe": "漯河",
        "Anyang": "安阳",
        "Xinxiang": "新乡",
        "Zhoukou": "周口",
        "Sanmenxia": "三门峡",
        "Jiaozuo": "焦作",
        "Pingdingshan": "平顶山",
        "Xinyang": "信阳",
        "Nanyang": "南阳",
        "Hebi": "鹤壁",
        "Puyang": "濮阳",
        "Xuchang": "许昌",
        "Shangqiu": "商丘",
        "Zhumadian": "驻马店",
        "Taiyuan": "太原",
        "DaTong": "大同",
        "Xinzhou": "忻州",
        "Yangquan": "阳泉",
        "Changzhi": "长治",
        "Jincheng": "晋城",
        "Shuozhou": "朔州",
        "Jinzhong": "晋中",
        "Yuncheng": "运城",
        "Linfen": "临汾",
        "Lvliang": "吕梁",
        "Xian": "西安",
        "Xianyang": "咸阳",
        "Tongchuan": "铜川",
        "Yanan": "延安",
        "Baoji": "宝鸡",
        "Weinan": "渭南",
        "Hanzhoung": "汉中",
        "Ankang": "安康",
        "Shangluo": "商洛",
        "Yulin": "榆林",
        "Lanzhou": "兰州",
        "Tianshui": "天水",
        "Pingliang": "平凉",
        "Jiuquan": "酒泉",
        "Jiayuguan": "嘉峪关",
        "Jinchang": "金昌",
        "baiyiin": "白银",
        "Wuwei": "武威",
        "Zhangye": "张掖",
        "Qingyang": "庆阳",
        "Dingxi": "定西",
        "Longnan": "陇南",
        "Xining": "西宁",
        "Nanchang": "南昌",
        "Jiujiang": "九江",
        "Ganzhou": "赣州",
        "Jian": "吉安",
        "Yingtan": "鹰潭",
        "Shangrao": "上饶",
        "Pingxiang": "萍乡",
        "Jingdezhen": "景德镇",
        "Xinyu": "新余",
        "Yichun": "宜春",
        "Fuzhou": "抚州"
}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# 发送请求
def main(city):
 list_href=[]
 list_all=[] 
 for year in range(2011,2023):
   for month in range(1,13):
      if month<10:
       list_href.append('https://lishi.tianqi.com/'+city+'/'+str(year)+'0'+str(month)+'.html')
      else:
         list_href.append('https://lishi.tianqi.com/'+city+'/'+str(year)+str(month)+'.html')  
 for href in list_href:
  try:
   response=requests.get(href,headers=headers)
   print(response.status_code)
   source=response.text
   data_get(source,list_all)

  except:
     to_csv(list_all,city)
     return 0
  to_csv(list_all,city)
  
def data_get(source,list_all):
 html=etree.HTML(source)
 li_list=html.xpath('/html/body//ul[@class="thrui"]//li')
 for li in li_list: 
    list_all.append(li.xpath('.//div/text()'))
    

def to_csv(list_all,city='Unkown'):
 load='./'+city+'_wea.csv'
 dic_all={}
 value_date=[]
 value_highest=[]
 value_lowest=[]
 value_weather=[]
 value_wind=[]
 for day in list_all:
  value_date.append(day[0])
  value_highest.append(day[1])
  value_lowest.append(day[2])
  value_weather.append(day[3])
  value_wind.append(day[4])
 dic_all['date']=value_date
 dic_all['highest']=value_highest
 dic_all['lowest']=value_lowest
 dic_all['weather']=value_weather
 dic_all['wind']=value_wind
 df=pd.DataFrame(dic_all)#df方法传入字典时其value必须是可迭代序列（如列表）
 df.to_csv(load)
 
 
for city in city_cn.keys():
 main(city)