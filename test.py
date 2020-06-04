# User(親クラス) -> AdminUser(サブクラス)
class User:

    """ 親クラスのコンストラクタ """
    #selfはクラスのインスタンス自身
    def __init__(self,name):
        self.name= name

    """ 親クラスのメソッド """
    def say_hi(self):
        print("[親クラスのメソッド]Hi! {0}".format(self.name))

# クラスの継承
class AdminUser(User):
    def __init__(self,name,age):
        """
        親クラス(Userの)__init__ メソッド
        (コンストラクタ)で
        name を初期化する処理がすでに存在するので、
        それをサブクラス(AdminUser)の中でも再利用を
        する為にsuper()を使う。
        """
        #これを呼び出す事で`self.name`が使える。
        # つまりここは、親クラスのself.nameと同じ場所を参照している。
        super().__init__(name)

        self.age = age

        #親クラスのプロパティを書き換える前。
        print("子クラスでsuper()を使った親クラスのプロパティ呼び出すされるnameは{0}".format(self.name))

        #親クラスのプロパティを書き換える。
        self.name = "Endo"
        print("子クラスで親クラスのプロパティを書き換えた後に呼び出されるname>は{}".format(self.name))

    # インスタンスメソッド
    def say_hello(self):
        print("Hello!! {0} age:{1}".format(self.name, self.age))

print("継承前の世界")
bob = User("Bob")
bob.say_hi()

print("継承後の世界")
bob = AdminUser("bob",22)
bob.say_hi()

print(bob.name)
# 小クラス(サブクラス)のインスタンスメソッド
bob.say_hello()
bob.say_hi()