# 디미고 커플 탐색기

잔류자 목록을 기반으로 디미고 내의 커플을 탐지하는 ```Python Script```입니다.  

# Installation

```bash
sudo apt install python2.7 python-pip
pip install requests
git clone https://github.com/ch4n3-yoon/dimigo-Couple-Searching.git
```



# Description

```Dimigo Life```로부터 잔류자 목록을 불러오고, 잔류 중 **_3번 이상 옆자리에 앉았_**을 경우 커플로 판단합니다. 제가 추측하는 정확도는 약 **30%**입니다. (남여 사이의 관계가 친할 경우 같이 앉는 경우도 있을 것이기 때문에 부정확입니다.)  



# How to execute?

1. ```Dimigo Life```에서 로그인을 한 뒤, ```JWT 코드```를 받아온다. 

   ```bash
   curl -X POST "https://api.dimigo.life/users/login" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "id=YOUR_ID&pwd=YOUR_PWD"
   ```

2. 받은 토큰 값을 ```authkey.py``` 의 ```authkey``` 변수에 넣는다. 

3. 파이썬으로 실행시킨다.

   ```bash
   # Linux
   chmod +x app.py
   ./app.py
   ```

   or

   ```bash
   python app.py 
   ```

4. 학생부 선생님들께 제보한다. 

