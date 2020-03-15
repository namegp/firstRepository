import  requests;
import  re;


if __name__=="__main__":


    url1 = "https://www.17k.com/chapter/2932117/36683845.html";
    response1 = requests.get(url1);
    response1.encoding = "utf-8";
    html1 = response1.text;
    # print(html1);


    a=re.findall(r'<div class="p">(.*?)</div>',html1,re.S);
    print(a);

    b=re.findall(r'<p>(.*?)</p>',html1,re.S);
    # print(b);





    # for num in range(80):
    #     print(re.findall(r'<p>(.*?)</p>',html1,re.S)[num]);

    #
    # file=open("九龙拉棺.txt","a",encoding="utf-8");
    # for num in range(80):
    #     file.write(re.findall(r'<p>(.*?)</p>',html1,re.S)[num]);

































