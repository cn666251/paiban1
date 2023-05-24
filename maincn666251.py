import random
import tkinter as tk
from tkinter import messagebox


# 定义员工类，包含员工编号，姓名，年龄，账号密码，所属值班室等属性
class Employee:
    def __init__(self, id, name, age, password, room):
        self.id = id  # 员工编号
        self.name = name  # 姓名
        self.age = age  # 年龄
        self.password = password  # 账号密码
        self.room = room  # 所属值班室

    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.age}\t{self.room}"


# 定义排班管理系统类，包含员工列表，当前登录的员工，当前显示的值班表等属性
class ScheduleSystem:
    def __init__(self):
        self.main_frame = None
        self.info_frame = None
        self.password_frame = None
        self.old_password_entry = None
        self.new_password_entry = None
        self.schedule_frame = None
        self.schedule_text = None
        self.time_frame = None
        self.time_var = None
        self.info_manage_frame = None
        self.add_frame = None
        self.add_id_entry = None
        self.add_name_entry = None
        self.add_age_entry = None
        self.add_password_entry = None
        self.add_room_var = None
        self.edit_frame = None
        self.edit_id_entry = None
        self.edit_employee = None
        self.edit_info_frame = None
        self.edit_var = None
        self.new_value_entry = None
        self.delete_frame = None
        self.delete_id_entry = None
        self.delete_employee = None
        self.search_frame = None
        self.search_var = None
        self.value_entry = None
        self.result_text = None
        self.sort_frame = None
        self.sort_var = None
        self.order_var = None
        self.result_text = None
        self.apply_frame = None
        self.apply_time_var = None
        self.apply_room_var = None
        self.auto_frame = None
        self.auto_room_var = None
        self.check_frame = None
        self.apply_text = None
        self.view_frame = None
        self.schedule_text = None
        self.applies = None
        self.schedule_2 = None
        self.schedule_1 = None
        self.manual_schedule = None
        self.employees = []  # 员工列表
        self.current_user = None  # 当前登录的员工
        self.current_schedule = {}  # 当前显示的值班表

        # 初始化员工列表，添加30个员工对象
        for i in range(1, 31):
            id = f"E{i:02d}"  # 生成员工编号，如E01, E02, ..., E30
            name = f"员工{i}"  # 生成员工姓名，如员工1, 员工2, ..., 员工30
            age = random.randint(20, 50)  # 生成员工年龄，随机在20到50之间
            password = "123456"  # 初始密码为123456
            if i <= 6:  # 如果是前6个员工，则属于第一值班室
                room = "第一值班室"
            elif i <= 12:  # 如果是第7到第12个员工，则属于第二值班室
                room = "第二值班室"
            elif i <= 18:  # 如果是第13到第18个员工，则属于第三值班室
                room = "第三值班室"
            elif i <= 24:  # 如果是第19到第24个员工，则属于第四值班室
                room = "第四值班室"
            else:  # 如果是最后6个员工，则属于行政值班室
                room = "行政值班室"
            employee = Employee(id, name, age, password, room)  # 创建员工对象
            self.employees.append(employee)  # 将员工对象添加到员工列表中

        # 将最后6个员工中的前两个设为总管理员，后四个设为排班管理员，并修改他们的姓名和密码
        self.employees[-6].name = "总管理员1"
        self.employees[-6].password = "admin1"
        self.employees[-5].name = "总管理员2"
        self.employees[-5].password = "admin2"
        self.employees[-4].name = "排班管理员1"
        self.employees[-4].password = "manager1"
        self.employees[-3].name = "排班管理员2"
        self.employees[-3].password = "manager2"
        self.employees[-2].name = "排班管理员3"
        self.employees[-2].password = "manager3"
        self.employees[-1].name = "排班管理员4"
        self.employees[-1].password = "manager4"

        # 创建图形用户界面窗口，并设置标题和大小
        self.window = tk.Tk()
        self.window.title("排班管理系统")
        self.window.geometry("800x600")

        # 创建登录界面的组件，并放置在窗口中
        self.login_frame = tk.Frame(self.window)  # 登录界面的框架
        self.login_frame.pack()
        tk.Label(self.login_frame, text="欢迎使用排班管理系统，请输入您的账号和密码", font=("宋体", 16)).pack(pady=20)
        tk.Label(self.login_frame, text="账号：", font=("宋体", 14)).pack()
        self.id_entry = tk.Entry(self.login_frame)  # 账号输入框
        self.id_entry.pack()
        tk.Label(self.login_frame, text="密码：", font=("宋体", 14)).pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")  # 密码输入框，显示为*
        self.password_entry.pack()
        tk.Button(self.login_frame, text="登录", font=("宋体", 14), command=self.login).pack(
            pady=10)  # 登录按钮，点击后调用login方法

    def login(self):
        """登录方法，验证账号和密码是否正确，并根据不同的权限进入不同的界面"""

        id = self.id_entry.get()  # 获取账号输入框中的内容
        password = self.password_entry.get()  # 获取密码输入框中的内容

        for employee in self.employees:  # 遍历员工列表中的每个员工对象
            if employee.id == id and employee.password == password:  # 如果找到匹配的账号和密码
                messagebox.showinfo("提示", f"登录成功，欢迎{employee.name}")  # 弹出提示框显示登录成功信息
                self.current_user = employee  # 将当前登录的员工设为该员工对象
                break  # 跳出循环
        else:  # 如果没有找到匹配的账号和密码
            messagebox.showerror("错误", "账号或密码错误，请重新输入")  # 弹出错误框显示错误信息
            return  # 返回

    # 继续定义排班管理系统类的方法

    def main_menu(self):
        """主菜单方法，根据当前登录的员工的权限，显示不同的选项，并调用相应的方法"""

        self.login_frame.pack_forget()  # 隐藏登录界面的框架
        self.main_frame = tk.Frame(self.window)  # 创建主菜单界面的框架
        self.main_frame.pack()
        tk.Label(self.main_frame, text=f"欢迎{self.current_user.name}，您所属的值班室是{self.current_user.room}",
                 font=("宋体", 16)).pack(pady=20)
        tk.Button(self.main_frame, text="查看个人信息", font=("宋体", 14), command=self.show_info).pack(
            pady=10)  # 查看个人信息按钮，点击后调用show_info方法
        tk.Button(self.main_frame, text="修改密码", font=("宋体", 14), command=self.change_password).pack(
            pady=10)  # 修改密码按钮，点击后调用change_password方法
        tk.Button(self.main_frame, text="查看值班表", font=("宋体", 14), command=self.show_schedule).pack(
            pady=10)  # 查看值班表按钮，点击后调用show_schedule方法
        if self.current_user.room == "行政值班室":  # 如果当前登录的员工属于行政值班室
            tk.Button(self.main_frame, text="管理员工信息", font=("宋体", 14), command=self.manage_info).pack(
                pady=10)  # 管理员工信息按钮，点击后调用manage_info方法
            tk.Button(self.main_frame, text="自动排班", font=("宋体", 14), command=self.auto_schedule).pack(
                pady=10)  # 自动排班按钮，点击后调用auto_schedule方法
            tk.Button(self.main_frame, text="手动调班", font=("宋体", 14), command=self.manual_schedule).pack(
                pady=10)  # 手动调班按钮，点击后调用manual_schedule方法
        else:  # 如果当前登录的员工不属于行政值班室
            tk.Button(self.main_frame, text="申请调班", font=("宋体", 14), command=self.apply_schedule).pack(
                pady=10)  # 申请调班按钮，点击后调用apply_schedule方法

    def show_info(self):
        """查看个人信息方法，显示当前登录的员工的信息"""

        self.main_frame.pack_forget()  # 隐藏主菜单界面的框架
        self.info_frame = tk.Frame(self.window)  # 创建查看个人信息界面的框架
        self.info_frame.pack()
        tk.Label(self.info_frame, text=f"您的个人信息如下：\n{self.current_user}", font=("宋体", 16)).pack(pady=20)
        tk.Button(self.info_frame, text="返回主菜单", font=("宋体", 14), command=self.back_to_main).pack(
            pady=10)  # 返回主菜单按钮，点击后调用back_to_main方法

    def change_password(self):
        """修改密码方法，让当前登录的员工输入旧密码和新密码，并验证是否正确"""

        self.main_frame.pack_forget()  # 隐藏主菜单界面的框架
        self.password_frame = tk.Frame(self.window)  # 创建修改密码界面的框架
        self.password_frame.pack()
        tk.Label(self.password_frame, text="请输入您的旧密码和新密码：", font=("宋体", 16)).pack(pady=20)
        tk.Label(self.password_frame, text="旧密码：", font=("宋体", 14)).pack()
        self.old_password_entry = tk.Entry(self.password_frame, show="*")  # 旧密码输入框，显示为*
        self.old_password_entry.pack()
        tk.Label(self.password_frame, text="新密码：", font=("宋体", 14)).pack()
        self.new_password_entry = tk.Entry(self.password_frame, show="*")  # 新密码输入框，显示为*
        self.new_password_entry.pack()
        tk.Button(self.password_frame, text="确认修改", font=("宋体", 14), command=self.confirm_password).pack(
            pady=10)  # 确认修改按钮，点击后调用confirm_password方法

    def confirm_password(self):
        """确认修改密码方法，检查旧密码是否正确，并更新新密码"""

        old_password = self.old_password_entry.get()  # 获取旧密码输入框中的内容
        new_password = self.new_password_entry.get()  # 获取新密码输入框中的内容

        if old_password == self.current_user.password:  # 如果旧密码正确
            if new_password:  # 如果新密码不为空
                self.current_user.password = new_password  # 将当前登录的员工的密码更新为新密码
                messagebox.showinfo("提示", "修改成功")  # 弹出提示框显示修改成功信息
                self.back_to_main()  # 调用back_to_main方法返回主菜单界面
            else:  # 如果新密码为空
                messagebox.showerror("错误", "新密码不能为空")  # 弹出错误框显示错误信息
                return  # 返回
        else:  # 如果旧密码错误
            messagebox.showerror("错误", "旧密码错误，请重新输入")  # 弹出错误框显示错误信息
            return  # 返回

    def show_schedule(self):
        """查看值班表方法，显示当前显示的值班表，并根据权限提供不同的选项"""

        self.main_frame.pack_forget() # 隐藏主菜单界面的框架
        self.schedule_frame = tk.Frame(self.window) # 创建查看值班表界面的框架
        self.schedule_frame.pack()
        tk.Label(self.schedule_frame, text="当前的值班表如下：", font=("宋体", 16)).pack(pady=20)
        self.schedule_text = tk.Text(self.schedule_frame) # 创建值班表文本框，用于显示值班表
        self.schedule_text.pack()
        for time, rooms in self.current_schedule.items(): # 遍历当前显示的值班表中的每个时间段和对应的值班室列表
            self.schedule_text.insert(tk.END, f"{time}：\n") # 在文本框中插入时间段
            for room, employees in rooms.items(): # 遍历每个值班室和对应的员工列表
                self.schedule_text.insert(tk.END, f"{room}：") # 在文本框中插入值班室
                for employee in employees: # 遍历每个员工
                    self.schedule_text.insert(tk.END, f"{employee.name} ") # 在文本框中插入员工姓名
                self.schedule_text.insert(tk.END, "\n") # 在文本框中换行
            self.schedule_text.insert(tk.END, "\n") # 在文本框中换行
        tk.Button(self.schedule_frame, text="返回主菜单", font=("宋体", 14), command=self.back_to_main).pack(pady=10) # 返回主菜单按钮，点击后调用back_to_main方法
        if self.current_user.room == "行政值班室": # 如果当前登录的员工属于行政值班室
            tk.Button(self.schedule_frame, text="切换时间段", font=("宋体", 14), command=self.switch_time).pack(pady=10) # 切换时间段按钮，点击后调用switch_time方法

    def back_to_main(self):
        """返回主菜单方法，隐藏当前界面的框架，并显示主菜单界面的框架"""

        self.info_frame.pack_forget() # 隐藏查看个人信息界面的框架
        self.password_frame.pack_forget() # 隐藏修改密码界面的框架
        self.schedule_frame.pack_forget() # 隐藏查看值班表界面的框架
        self.info_manage_frame.pack_forget() # 隐藏管理员工信息界面的框架
        self.apply_frame.pack_forget() # 隐藏申请调班界面的框架
        self.main_frame.pack() # 显示主菜单界面的框架

    def switch_time(self):
        """切换时间段方法，让当前登录的员工选择要查看的时间段，并更新当前显示的值班表"""

        self.schedule_frame.pack_forget() # 隐藏查看值班表界面的框架
        self.time_frame = tk.Frame(self.window) # 创建切换时间段界面的框架
        self.time_frame.pack()
        tk.Label(self.time_frame, text="请选择要查看的时间段：", font=("宋体", 16)).pack(pady=20)
        self.time_var = tk.StringVar() # 创建一个字符串变量，用于存储选择的时间段
        self.time_var.set("9:00到18:00") # 设置初始值为9:00到18:00
        tk.Radiobutton(self.time_frame, text="9:00到18:00", font=("宋体", 14), variable=self.time_var, value="9:00到18:00").pack() # 创建单选按钮，选择9:00到18:00
        tk.Radiobutton(self.time_frame, text="18:00到9:00", font=("宋体", 14), variable=self.time_var, value="18:00到9:00").pack() # 创建单选按钮，选择18:00到9:00
        tk.Button(self.time_frame, text="确认切换", font=("宋体", 14), command=self.confirm_time).pack(pady=10) # 确认切换按钮，点击后调用confirm_time方法

    def confirm_time(self):
        """确认切换时间段方法，根据选择的时间段，更新当前显示的值班表，并返回查看值班表界面"""

        time = self.time_var.get() # 获取选择的时间段
        if time == "9:00到18:00": # 如果选择的是9:00到18:00
            self.current_schedule = self.schedule_1 # 将当前显示的值班表设为第一个值班表
        else: # 如果选择的是18:00到9:00
            self.current_schedule = self.schedule_2 # 将当前显示的值班表设为第二个值班表
        messagebox.showinfo("提示", f"已切换到{time}的值班表") # 弹出提示框显示切换成功信息
        self.time_frame.pack_forget() # 隐藏切换时间段界面的框架
        self.show_schedule() # 调用show_schedule方法显示值班表界面

    def manage_info(self):
        """管理员工信息方法，根据当前登录的员工的权限，显示不同的选项，并调用相应的方法"""

        self.main_frame.pack_forget() # 隐藏主菜单界面的框架
        self.info_manage_frame = tk.Frame(self.window) # 创建管理员工信息界面的框架
        self.info_manage_frame.pack()
        tk.Label(self.info_manage_frame, text="请选择要进行的操作：", font=("宋体", 16)).pack(pady=20)
        tk.Button(self.info_manage_frame, text="增加员工信息", font=("宋体", 14), command=self.add_info).pack(pady=10) # 增加员工信息按钮，点击后调用add_info方法
        tk.Button(self.info_manage_frame, text="修改员工信息", font=("宋体", 14), command=self.edit_info).pack(pady=10) # 修改员工信息按钮，点击后调用edit_info方法
        tk.Button(self.info_manage_frame, text="删除员工信息", font=("宋体", 14), command=self.delete_info).pack(pady=10) # 删除员工信息按钮，点击后调用delete_info方法
        tk.Button(self.info_manage_frame, text="查询员工信息", font=("宋体", 14), command=self.search_info).pack(pady=10) # 查询员工信息按钮，点击后调用search_info方法
        tk.Button(self.info_manage_frame, text="排序员工信息", font=("宋体", 14), command=self.sort_info).pack(pady=10) # 排序员工信息按钮，点击后调用sort_info方法
        tk.Button(self.info_manage_frame, text="返回主菜单", font=("宋体", 14), command=self.back_to_main).pack(pady=10) # 返回主菜单按钮，点击后调用back_to_main方法

    def add_info(self):
        """增加员工信息方法，让当前登录的员工输入要增加的员工的信息，并验证是否合法"""

        self.info_manage_frame.pack_forget() # 隐藏管理员工信息界面的框架
        self.add_frame = tk.Frame(self.window) # 创建增加员工信息界面的框架
        self.add_frame.pack()
        tk.Label(self.add_frame, text="请输入要增加的员工的信息：", font=("宋体", 16)).pack(pady=20)
        tk.Label(self.add_frame, text="员工编号：", font=("宋体", 14)).pack()
        self.add_id_entry = tk.Entry(self.add_frame) # 员工编号输入框
        self.add_id_entry.pack()
        tk.Label(self.add_frame, text="姓名：", font=("宋体", 14)).pack()
        self.add_name_entry = tk.Entry(self.add_frame) # 姓名输入框
        self.add_name_entry.pack()
        tk.Label(self.add_frame, text="年龄：", font=("宋体", 14)).pack()
        self.add_age_entry = tk.Entry(self.add_frame) # 年龄输入框
        self.add_age_entry.pack()
        tk.Label(self.add_frame, text="密码：", font=("宋体", 14)).pack()
        self.add_password_entry = tk.Entry(self.add_frame) # 密码输入框
        self.add_password_entry.pack()
        tk.Label(self.add_frame, text="所属值班室：", font=("宋体", 14)).pack()
        self.add_room_var = tk.StringVar() # 创建一个字符串变量，用于存储选择的值班室
        if self.current_user.name.startswith("总管理员"): # 如果当前登录的员工是总管理员
            self.add_room_var.set("第一值班室") # 设置初始值为第一值班室
            tk.OptionMenu(self.add_frame, self.add_room_var, "第一值班室", "第二值班室", "第三值班室", "第四值班室").pack() # 创建下拉菜单，可以选择第一到第四值班室
        else: # 如果当前登录的员工是排班管理员
            room = self.current_user.room.replace("排班管理员", "值班室") # 获取当前登录的员工所管的值班室
            self.add_room_var.set(room) # 设置初始值为该值班室
            tk.OptionMenu(self.add_frame, self.add_room_var, room).pack() # 创建下拉菜单，只能选择该值班室
        tk.Button(self.add_frame, text="确认增加", font=("宋体", 14), command=self.confirm_add).pack(pady=10) # 确认增加按钮，点击后调用confirm_add方法

    def confirm_add(self):
        """确认增加员工信息方法，检查输入的信息是否合法，并添加到员工列表中"""

        id = self.add_id_entry.get() # 获取员工编号输入框中的内容
        name = self.add_name_entry.get() # 获取姓名输入框中的内容
        age = self.add_age_entry.get() # 获取年龄输入框中的内容
        password = self.add_password_entry.get() # 获取密码输入框中的内容
        room = self.add_room_var.get() # 获取选择的值班室

        if not id or not name or not age or not password: # 如果有任何一个输入为空
            messagebox.showerror("错误", "请输入完整的信息") # 弹出错误框显示错误信息
            return # 返回

        if not id.startswith("E") or not id[1:].isdigit(): # 如果员工编号不是以E开头或后面不是数字
            messagebox.showerror("错误", "员工编号格式不正确") # 弹出错误框显示错误信息
            return # 返回

        for employee in self.employees: # 遍历员工列表中的每个员工对象
            if employee.id == id: # 如果找到相同的员工编号
                messagebox.showerror("错误", "该员工编号已存在") # 弹出错误框显示错误信息
                return # 返回

        try: # 尝试将年龄转换为整数
            age = int(age)
            if age < 18 or age > 60: # 如果年龄不在18到60之间
                raise ValueError # 抛出异常
        except ValueError: # 捕获异常
            messagebox.showerror("错误", "年龄必须是18到60之间的整数") # 弹出错误框显示错误信息
            return # 返回

    # 继续定义排班管理系统类的方法

    def confirm_add(self):
        """确认增加员工信息方法，检查输入的信息是否合法，并添加到员工列表中"""

        id = self.add_id_entry.get()  # 获取员工编号输入框中的内容
        name = self.add_name_entry.get()  # 获取姓名输入框中的内容
        age = self.add_age_entry.get()  # 获取年龄输入框中的内容
        password = self.add_password_entry.get()  # 获取密码输入框中的内容
        room = self.add_room_var.get()  # 获取选择的值班室

        if not id or not name or not age or not password:  # 如果有任何一个输入为空
            messagebox.showerror("错误", "请输入完整的信息")  # 弹出错误框显示错误信息
            return  # 返回

        if not id.startswith("E") or not id[1:].isdigit():  # 如果员工编号不是以E开头或后面不是数字
            messagebox.showerror("错误", "员工编号格式不正确")  # 弹出错误框显示错误信息
            return  # 返回

        for employee in self.employees:  # 遍历员工列表中的每个员工对象
            if employee.id == id:  # 如果找到相同的员工编号
                messagebox.showerror("错误", "该员工编号已存在")  # 弹出错误框显示错误信息
                return  # 返回

        try:  # 尝试将年龄转换为整数
            age = int(age)
            if age < 18 or age > 60:  # 如果年龄不在18到60之间
                raise ValueError  # 抛出异常
        except ValueError:  # 捕获异常
            messagebox.showerror("错误", "年龄必须是18到60之间的整数")  # 弹出错误框显示错误信息
            return  # 返回

        employee = Employee(id, name, age, password, room)  # 创建新的员工对象
        self.employees.append(employee)  # 将新的员工对象添加到员工列表中
        messagebox.showinfo("提示", "增加成功")  # 弹出提示框显示增加成功信息
        self.back_to_manage()  # 调用back_to_manage方法返回管理员工信息界面

    def back_to_manage(self):
        """返回管理员工信息界面方法，隐藏当前界面的框架，并显示管理员工信息界面的框架"""

        self.add_frame.pack_forget()  # 隐藏增加员工信息界面的框架
        self.edit_frame.pack_forget()  # 隐藏修改员工信息界面的框架
        self.delete_frame.pack_forget()  # 隐藏删除员工信息界面的框架
        self.search_frame.pack_forget()  # 隐藏查询员工信息界面的框架
        self.sort_frame.pack_forget()  # 隐藏排序员工信息界面的框架
        self.info_manage_frame.pack()  # 显示管理员工信息界面的框架

    def edit_info(self):
        """修改员工信息方法，让当前登录的员工输入要修改的员工编号，并显示该员工的信息"""

        self.info_manage_frame.pack_forget()  # 隐藏管理员工信息界面的框架
        self.edit_frame = tk.Frame(self.window)  # 创建修改员工信息界面的框架
        self.edit_frame.pack()
        tk.Label(self.edit_frame, text="请输入要修改的员工编号：", font=("宋体", 16)).pack(pady=20)
        self.edit_id_entry = tk.Entry(self.edit_frame)  # 员工编号输入框
        self.edit_id_entry.pack()
        tk.Button(self.edit_frame, text="确认修改", font=("宋体", 14), command=self.confirm_edit).pack(
            pady=10)  # 确认修改按钮，点击后调用confirm_edit方法

    def confirm_edit(self):
        """确认修改员工信息方法，检查输入的员工编号是否存在，并显示该员工的信息，并提供修改选项"""

        id = self.edit_id_entry.get()  # 获取员工编号输入框中的内容

        if not id:  # 如果输入为空
            messagebox.showerror("错误", "请输入员工编号")  # 弹出错误框显示错误信息
            return  # 返回

        for employee in self.employees:  # 遍历员工列表中的每个员工对象
            if employee.id == id:  # 如果找到匹配的员工编号
                self.edit_employee = employee  # 将要修改的员工设为该员工对象
                break  # 跳出循环
        else:  # 如果没有找到匹配的员工编号
            messagebox.showerror("错误", "该员工编号不存在")  # 弹出错误框显示错误信息
            return  # 返回

        self.edit_frame.pack_forget()  # 隐藏修改员工信息界面的框架
        self.edit_info_frame = tk.Frame(self.window)  # 创建修改员工具体信息界面的框架
        self.edit_info_frame.pack()
        tk.Label(self.edit_info_frame, text=f"您要修改的员工信息如下：\n{self.edit_employee}", font=("宋体", 16)).pack(
            pady=20)
        tk.Label(self.edit_info_frame, text="请选择要修改的属性：", font=("宋体", 14)).pack()
        self.edit_var = tk.StringVar()  # 创建一个字符串变量，用于存储选择的属性
        self.edit_var.set("姓名")  # 设置初始值为姓名
        tk.OptionMenu(self.edit_info_frame, self.edit_var, "姓名", "年龄", "密码").pack()  # 创建下拉菜单，可以选择姓名，年龄，密码
        tk.Label(self.edit_info_frame, text="请输入新的值：", font=("宋体", 14)).pack()
        self.new_value_entry = tk.Entry(self.edit_info_frame)  # 新值输入框
        self.new_value_entry.pack()
        tk.Button(self.edit_info_frame, text="确认修改", font=("宋体", 14), command=self.update_info).pack(
            pady=10)  # 确认修改按钮，点击后调用update_info方法

    def update_info(self):
        """更新员工信息方法，根据选择的属性和输入的新值，更新要修改的员工对象，并检查是否合法"""


        attribute = self.edit_var.get() # 获取选择的属性
        new_value = self.new_value_entry.get() # 获取新值输入框中的内容

        if not new_value: # 如果输入为空
            messagebox.showerror("错误", "请输入新的值") # 弹出错误框显示错误信息
            return # 返回

        if attribute == "姓名": # 如果选择的是姓名
            self.edit_employee.name = new_value # 将要修改的员工对象的姓名更新为新值
        elif attribute == "年龄": # 如果选择的是年龄
            try: # 尝试将新值转换为整数
                new_value = int(new_value)
                if new_value < 18 or new_value > 60: # 如果新值不在18到60之间
                    raise ValueError # 抛出异常
            except ValueError: # 捕获异常
                messagebox.showerror("错误", "年龄必须是18到60之间的整数") # 弹出错误框显示错误信息
                return # 返回
            self.edit_employee.age = new_value # 将要修改的员工对象的年龄更新为新值
        else: # 如果选择的是密码
            self.edit_employee.password = new_value # 将要修改的员工对象的密码更新为新值

        messagebox.showinfo("提示", "修改成功") # 弹出提示框显示修改成功信息
        self.back_to_manage() # 调用back_to_manage方法返回管理员工信息界面

    def delete_info(self):
        """删除员工信息方法，让当前登录的员工输入要删除的员工编号，并验证是否存在"""

        self.info_manage_frame.pack_forget() # 隐藏管理员工信息界面的框架
        self.delete_frame = tk.Frame(self.window) # 创建删除员工信息界面的框架
        self.delete_frame.pack()
        tk.Label(self.delete_frame, text="请输入要删除的员工编号：", font=("宋体", 16)).pack(pady=20)
        self.delete_id_entry = tk.Entry(self.delete_frame) # 员工编号输入框
        self.delete_id_entry.pack()
        tk.Button(self.delete_frame, text="确认删除", font=("宋体", 14), command=self.confirm_delete).pack(pady=10) # 确认删除按钮，点击后调用confirm_delete方法

    def confirm_delete(self):
        """确认删除员工信息方法，检查输入的员工编号是否存在，并从员工列表中删除该员工对象"""

        id = self.delete_id_entry.get() # 获取员工编号输入框中的内容

        if not id: # 如果输入为空
            messagebox.showerror("错误", "请输入员工编号") # 弹出错误框显示错误信息
            return # 返回

        for employee in self.employees: # 遍历员工列表中的每个员工对象
            if employee.id == id: # 如果找到匹配的员工编号
                self.delete_employee = employee # 将要删除的员工设为该员工对象
                break # 跳出循环
        else: # 如果没有找到匹配的员工编号
            messagebox.showerror("错误", "该员工编号不存在") # 弹出错误框显示错误信息
            return # 返回

        if self.current_user.name.startswith("总管理员"): # 如果当前登录的员工是总管理员
            pass # 不做任何限制
        else: # 如果当前登录的员工是排班管理员
            room = self.current_user.room.replace("排班管理员", "值班室") # 获取当前登录的员工所管的值班室
            if self.delete_employee.room != room: # 如果要删除的员工不属于该值班室
                messagebox.showerror("错误", "您没有权限删除其他值班室的员工") # 弹出错误框显示错误信息
                return # 返回

        answer = messagebox.askyesno("提示", f"您确定要删除{self.delete_employee.name}吗？") # 弹出确认框询问是否确定删除
        if answer: # 如果回答是
            self.employees.remove(self.delete_employee) # 从员工列表中移除该员工对象
            messagebox.showinfo("提示", "删除成功") # 弹出提示框显示删除成功信息
            self.back_to_manage() # 调用back_to_manage方法返回管理员工信息界面

    def search_info(self):
        """查询员工信息方法，让当前登录的员工输入要查询的条件，并显示符合条件的员工信息"""

        self.info_manage_frame.pack_forget()  # 隐藏管理员工信息界面的框架
        self.search_frame = tk.Frame(self.window)  # 创建查询员工信息界面的框架
        self.search_frame.pack()
        tk.Label(self.search_frame, text="请输入要查询的条件：", font=("宋体", 16)).pack(pady=20)
        tk.Label(self.search_frame, text="属性：", font=("宋体", 14)).pack()
        self.search_var = tk.StringVar()  # 创建一个字符串变量，用于存储选择的属性
        self.search_var.set("姓名")  # 设置初始值为姓名
        tk.OptionMenu(self.search_frame, self.search_var, "姓名", "年龄", "所属值班室").pack()  # 创建下拉菜单，可以选择姓名，年龄，所属值班室
        tk.Label(self.search_frame, text="值：", font=("宋体", 14)).pack()
        self.value_entry = tk.Entry(self.search_frame)  # 值输入框
        self.value_entry.pack()
        tk.Button(self.search_frame, text="确认查询", font=("宋体", 14), command=self.confirm_search).pack(
            pady=10)  # 确认查询按钮，点击后调用confirm_search方法

    def confirm_search(self):
        """确认查询员工信息方法，根据选择的属性和输入的值，筛选出符合条件的员工对象，并显示他们的信息"""

        attribute = self.search_var.get()  # 获取选择的属性
        value = self.value_entry.get()  # 获取值输入框中的内容

        if not value:  # 如果输入为空
            messagebox.showerror("错误", "请输入要查询的值")  # 弹出错误框显示错误信息
            return  # 返回

        if attribute == "年龄":  # 如果选择的是年龄
            try:  # 尝试将值转换为整数
                value = int(value)
                if value < 18 or value > 60:  # 如果值不在18到60之间
                    raise ValueError  # 抛出异常
            except ValueError:  # 捕获异常
                messagebox.showerror("错误", "年龄必须是18到60之间的整数")  # 弹出错误框显示错误信息
                return  # 返回

        result = []  # 创建一个空列表，用于存储符合条件的员工对象
        for employee in self.employees:  # 遍历员工列表中的每个员工对象
            if getattr(employee, attribute) == value:  # 如果该员工对象的属性与值相等
                result.append(employee)  # 将该员工对象添加到结果列表中

        if result:  # 如果结果列表不为空
            messagebox.showinfo("提示", f"共找到{len(result)}个符合条件的员工")  # 弹出提示框显示找到的数量
            self.result_text = tk.Text(self.search_frame)  # 创建结果文本框，用于显示结果列表中的员工信息
            self.result_text.pack()
            for employee in result:  # 遍历结果列表中的每个员工对象
                self.result_text.insert(tk.END, f"{employee}\n")  # 在文本框中插入员工信息并换行
            tk.Button(self.search_frame, text="返回管理界面", font=("宋体", 14), command=self.back_to_manage).pack(
                pady=10)  # 返回管理界面按钮，点击后调用back_to_manage方法
        else:  # 如果结果列表为空
            messagebox.showinfo("提示", "没有找到符合条件的员工")  # 弹出提示框显示没有找到信息

    def sort_info(self):
        """排序员工信息方法，让当前登录的员工选择要排序的属性和顺序，并显示排序后的员工信息"""

        self.info_manage_frame.pack_forget()  # 隐藏管理员工信息界面的框架
        self.sort_frame = tk.Frame(self.window)  # 创建排序员工信息界面的框架
        self.sort_frame.pack()
        tk.Label(self.sort_frame, text="请选择要排序的属性和顺序：", font=("宋体", 16)).pack(pady=20)
        tk.Label(self.sort_frame, text="属性：", font=("宋体", 14)).pack()
        self.sort_var = tk.StringVar()  # 创建一个字符串变量，用于存储选择的属性
        self.sort_var.set("员工编号")  # 设置初始值为员工编号
        tk.OptionMenu(self.sort_frame, self.sort_var, "员工编号", "姓名", "年龄").pack()  # 创建下拉菜单，可以选择员工编号，姓名，年龄
        tk.Label(self.sort_frame, text="顺序：", font=("宋体", 14)).pack()
        self.order_var = tk.StringVar()  # 创建一个字符串变量，用于存储选择的顺序
        self.order_var.set("升序")  # 设置初始值为升序
        tk.OptionMenu(self.sort_frame, self.order_var, "升序", "降序").pack()  # 创建下拉菜单，可以选择升序或降序
        tk.Button(self.sort_frame, text="确认排序", font=("宋体", 14), command=self.confirm_sort).pack(
            pady=10)  # 确认排序按钮，点击后调用confirm_sort方法

    def confirm_sort(self):
        """确认排序员工信息方法，根据选择的属性和顺序，对员工列表进行排序，并显示排序后的员工信息"""

        attribute = self.sort_var.get()  # 获取选择的属性
        order = self.order_var.get()  # 获取选择的顺序

        if attribute == "姓名":  # 如果选择的是姓名
            key = lambda employee: employee.name  # 定义排序的关键字为员工对象的姓名属性
        elif attribute == "年龄":  # 如果选择的是年龄
            key = lambda employee: employee.age  # 定义排序的关键字为员工对象的年龄属性
        else:  # 如果选择的是员工编号
            key = lambda employee: employee.id  # 定义排序的关键字为员工对象的编号属性

        if order == "升序":  # 如果选择的是升序
            reverse = False  # 定义排序的方向为不反转
        else:  # 如果选择的是降序
            reverse = True  # 定义排序的方向为反转

        self.employees.sort(key=key, reverse=reverse)  # 对员工列表进行排序

        messagebox.showinfo("提示", f"已按{attribute}{order}排好序")  # 弹出提示框显示排序成功信息
        self.result_text = tk.Text(self.sort_frame)  # 创建结果文本框，用于显示排序后的员工信息
        self.result_text.pack()
        for employee in self.employees:  # 遍历员工列表中的每个员工对象
            self.result_text.insert(tk.END, f"{employee}\n")  # 在文本框中插入员工信息并换行
        tk.Button(self.sort_frame, text="返回管理界面", font=("宋体", 14), command=self.back_to_manage).pack(
            pady=10)  # 返回管理界面按钮，点击后调用back_to_manage方法

    def apply_schedule(self):
        """申请调班方法，让当前登录的员工输入要调班的时间段和值班室，并验证是否合法"""

        self.main_frame.pack_forget()  # 隐藏主菜单界面的框架
        self.apply_frame = tk.Frame(self.window)  # 创建申请调班界面的框架
        self.apply_frame.pack()
        tk.Label(self.apply_frame, text="请输入要调班的时间段和值班室：", font=("宋体", 16)).pack(pady=20)
        tk.Label(self.apply_frame, text="时间段：", font=("宋体", 14)).pack()
        self.apply_time_var = tk.StringVar()  # 创建一个字符串变量，用于存储选择的时间段
        self.apply_time_var.set("9:00到18:00")  # 设置初始值为9:00到18:00
        tk.OptionMenu(self.apply_frame, self.apply_time_var, "9:00到18:00",
                      "18:00到9:00").pack()  # 创建下拉菜单，可以选择9:00到18:00或18:00到9:00
        tk.Label(self.apply_frame, text="值班室：", font=("宋体", 14)).pack()
        self.apply_room_var = tk.StringVar()  # 创建一个字符串变量，用于存储选择的值班室
        self.apply_room_var.set("第一值班室")  # 设置初始值为第一值班室
        tk.OptionMenu(self.apply_frame, self.apply_room_var, "第一值班室", "第二值班室", "第三值班室",
                      "第四值班室").pack()  # 创建下拉菜单，可以选择第一到第四值班室
        tk.Button(self.apply_frame, text="确认申请", font=("宋体", 14), command=self.confirm_apply).pack(
            pady=10)  # 确认申请按钮，点击后调用confirm_apply方法

    def confirm_apply(self):
        """确认申请调班方法，检查选择的时间段和值班室是否合法，并将申请添加到申请列表中"""

        time = self.apply_time_var.get()  # 获取选择的时间段
        room = self.apply_room_var.get()  # 获取选择的值班室

        if room == self.current_user.room:  # 如果选择的值班室与当前登录的员工所属的值班室相同
            messagebox.showerror("错误", "不能与自己所属的值班室调班")  # 弹出错误框显示错误信息
            return  # 返回

        if time == "9:00到18:00":  # 如果选择的是9:00到18:00
            schedule = self.schedule_1  # 将要查询的值班表设为第一个值班表
        else:  # 如果选择的是18:00到9:00
            schedule = self.schedule_2  # 将要查询的值班表设为第二个值班表

        if self.current_user not in schedule[time][self.current_user.room]:  # 如果当前登录的员工在该时间段该值班室没有排班
            messagebox.showerror("错误", "您在该时间段该值班室没有排班，不能申请调班")  # 弹出错误框显示错误信息
            return  # 返回

        if not schedule[time][room]:  # 如果该时间段该值班室没有员工排班
            messagebox.showerror("错误", "该时间段该值班室没有员工排班，不能申请调班")  # 弹出错误框显示错误信息
            return  # 返回

    def confirm_apply(self):
        """确认申请调班方法，检查选择的时间段和值班室是否合法，并将申请添加到申请列表中"""

        time = self.apply_time_var.get()  # 获取选择的时间段
        room = self.apply_room_var.get()  # 获取选择的值班室

        if room == self.current_user.room:  # 如果选择的值班室与当前登录的员工所属的值班室相同
            messagebox.showerror("错误", "不能与自己所属的值班室调班")  # 弹出错误框显示错误信息
            return  # 返回

        if time == "9:00到18:00":  # 如果选择的是9:00到18:00
            schedule = self.schedule_1  # 将要查询的值班表设为第一个值班表
        else:  # 如果选择的是18:00到9:00
            schedule = self.schedule_2  # 将要查询的值班表设为第二个值班表

        if self.current_user not in schedule[time][self.current_user.room]:  # 如果当前登录的员工在该时间段该值班室没有排班
            messagebox.showerror("错误", "您在该时间段该值班室没有排班，不能申请调班")  # 弹出错误框显示错误信息
            return  # 返回

        if not schedule[time][room]:  # 如果该时间段该值班室没有员工排班
            messagebox.showerror("错误", "该时间段该值班室没有员工排班，不能申请调班")  # 弹出错误框显示错误信息
            return  # 返回

        target_employee = schedule[time][room][0]  # 将要调班的目标员工设为该时间段该值班室排在第一个的员工对象
        apply = (self.current_user, target_employee, time)  # 创建一个元组，用于存储申请调班的信息
        self.applies.append(apply)  # 将申请调班的信息添加到申请列表中
        messagebox.showinfo("提示", f"已向{target_employee.name}发出申请，请等待对方回复")  # 弹出提示框显示申请成功信息
        self.back_to_main()  # 调用back_to_main方法返回主菜单界面

    def auto_schedule(self):
        """自动排班方法，根据当前登录的员工的权限，自动为每个值班室生成两个时间段的值班表，并保存到文件中"""

        self.main_frame.pack_forget()  # 隐藏主菜单界面的框架
        self.auto_frame = tk.Frame(self.window)  # 创建自动排班界面的框架
        self.auto_frame.pack()
        tk.Label(self.auto_frame, text="请选择要自动排班的值班室：", font=("宋体", 16)).pack(pady=20)
        self.auto_room_var = tk.StringVar()  # 创建一个字符串变量，用于存储选择的值班室
        if self.current_user.name.startswith("总管理员"):  # 如果当前登录的员工是总管理员
            self.auto_room_var.set("全部")  # 设置初始值为全部
            tk.OptionMenu(self.auto_frame, self.auto_room_var, "全部", "第一值班室", "第二值班室", "第三值班室",
                          "第四值班室").pack()  # 创建下拉菜单，可以选择全部或第一到第四值班室
        else:  # 如果当前登录的员工是排班管理员
            room = self.current_user.room.replace("排班管理员", "值班室")  # 获取当前登录的员工所管的值班室
            self.auto_room_var.set(room)  # 设置初始值为该值班室
            tk.OptionMenu(self.auto_frame, self.auto_room_var, room).pack()  # 创建下拉菜单，只能选择该值班室
        tk.Button(self.auto_frame, text="确认自动排班", font=("宋体", 14), command=self.confirm_auto).pack(
            pady=10)  # 确认自动排班按钮，点击后调用confirm_auto方法

    def confirm_auto(self):
        """确认自动排班方法，根据选择的值班室，随机分配员工到两个时间段，并更新相应的值班表，并保存到文件中"""

        room = self.auto_room_var.get()  # 获取选择的值班室

        if room == "全部":  # 如果选择的是全部
            rooms = ["第一值班室", "第二值班室", "第三值班室", "第四值班室"]  # 将要排班的值班室设为全部四个
        else:  # 如果选择的是某一个
            rooms = [room]  # 将要排班的值班室设为该一个

        for room in rooms:  # 遍历要排班的每个值班室
            employees = [employee for employee in self.employees if employee.room == room]  # 筛选出属于该值班室的员工对象列表
            random.shuffle(employees)  # 随机打乱员工对象列表
            half = len(employees) // 2  # 计算员工对象列表的一半长度
            schedule_1 = employees[:half]  # 将前一半分配到第一个时间段
            schedule_2 = employees[half:]  # 将后一半分配到第二个时间段
            self.schedule_1["9:00到18:00"][room] = schedule_1  # 更新第一个时间段对应该值班室的员工列表
            self.schedule_2["18:00到9:00"][room] = schedule_2  # 更新第二个时间段对应该值班室的员工列表

        with open("schedule_1.txt", "w") as f:  # 打开文件schedule_1.txt，以写入模式
            for time, rooms in self.schedule_1.items():  # 遍历第一个值班表中的每个时间段和对应的值班室列表
                f.write(f"{time}：\n")  # 在文件中写入时间段并换行
                for room, employees in rooms.items():  # 遍历每个值班室和对应的员工列表
                    f.write(f"{room}：")  # 在文件中写入值班室
                    for employee in employees:  # 遍历每个员工
                        f.write(f"{employee.name} ")  # 在文件中写入员工姓名
                    f.write("\n")  # 在文件中换行
                f.write("\n")  # 在文件中换行

        with open("schedule_2.txt", "w") as f:  # 打开文件schedule_2.txt，以写入模式
            for time, rooms in self.schedule_2.items():  # 遍历第二个值班表中的每个时间段和对应的值班室列表
                f.write(f"{time}：\n")  # 在文件中写入时间段并换行
                for room, employees in rooms.items():  # 遍历每个值班室和对应的员工列表
                    f.write(f"{room}：")  # 在文件中写入值班室
                    for employee in employees:  # 遍历每个员工
                        f.write(f"{employee.name} ")  # 在文件中写入员工姓名
                    f.write("\n")  # 在文件中换行
                f.write("\n")  # 在文件中换行

        messagebox.showinfo("提示", f"已为{room}自动排好两个时间段的值班表，并保存到文件中")  # 弹出提示框显示自动排好成功信息

    def back_to_main(self):
        """返回主菜单界面方法，隐藏当前界面的框架，并显示主菜单界面的框架"""

        self.apply_frame.pack_forget()  # 隐藏申请调班界面的框架
        self.auto_frame.pack_forget()  # 隐藏自动排班界面的框架
        self.main_frame.pack()  # 显示主菜单界面的框架

    def check_apply(self):
        """查看调班申请方法，显示当前登录的员工收到的调班申请，并提供同意或拒绝选项"""

        self.main_frame.pack_forget()  # 隐藏主菜单界面的框架
        self.check_frame = tk.Frame(self.window)  # 创建查看调班申请界面的框架
        self.check_frame.pack()
        tk.Label(self.check_frame, text="您收到的调班申请如下：", font=("宋体", 16)).pack(pady=20)
        self.apply_text = tk.Text(self.check_frame)  # 创建申请文本框，用于显示收到的申请信息
        self.apply_text.pack()
        for apply in self.applies:  # 遍历申请列表中的每个申请信息
            if apply[1] == self.current_user:  # 如果该申请信息中的目标员工是当前登录的员工
                self.apply_text.insert(tk.END, f"{apply[0].name}想在{apply[2]}与您调班\n")  # 在文本框中插入申请信息并换行
        tk.Button(self.check_frame, text="同意", font=("宋体", 14), command=self.agree_apply).pack(
            pady=10)  # 同意按钮，点击后调用agree_apply方法
        tk.Button(self.check_frame, text="拒绝", font=("宋体", 14), command=self.refuse_apply).pack(
            pady=10)  # 拒绝按钮，点击后调用refuse_apply方法

    def agree_apply(self):
        """同意调班申请方法，根据选择的申请信息，交换两个员工在相应时间段和值班室的排班，并更新相应的值班表，并保存到文件中"""

        index = int(self.apply_text.index(tk.INSERT).split(".")[0]) - 1  # 获取文本框中光标所在行数减一，作为选择的申请信息在申请列表中的索引
        apply = self.applies[index]  # 获取选择的申请信息

        if apply[2] == "9:00到18:00":  # 如果选择的是9:00到18:00
            schedule = self.schedule_1  # 将要修改的值班表设为第一个值班表
        else:  # 如果选择的是18:00到9:00
            schedule = self.schedule_2  # 将要修改的值班表设为第二个值班表

        source_employee = apply[0]  # 将要调班的源员工设为申请信息中的源员工对象
        target_employee = apply[1]  # 将要调班的目标员工设为申请信息中的目标员工对象

        schedule[apply[2]][source_employee.room].remove(source_employee)  # 从源员工所在时间段和值班室中移除源员工对象
        schedule[apply[2]][target_employee.room].remove(target_employee)  # 从目标员工所在时间段和值班室中移除目标员工对象

        schedule[apply[2]][source_employee.room].append(target_employee)  # 在源员工所在时间段和值班室中添加目标员工对象
        schedule[apply[2]][target_employee.room].append(source_employee)  # 在目标员工所在时间段和值班室中添加源员工对象

        with open("schedule_1.txt", "w") as f:  # 打开文件schedule_1.txt，以写入模式
            for time, rooms in self.schedule_1.items():  # 遍历第一个值班表中的每个时间段和对应的值班室列表
                f.write(f"{time}：\n")  # 在文件中写入时间段并换行
                for room, employees in rooms.items():  # 遍历每个值班室和对应的员工列表
                    f.write(f"{room}：")  # 在文件中写入值班室
                    for employee in employees:  # 遍历每个员工
                        f.write(f"{employee.name} ")  # 在文件中写入员工姓名
                    f.write("\n")  # 在文件中换行
                f.write("\n")  # 在文件中换行

        with open("schedule_2.txt", "w") as f:  # 打开文件schedule_2.txt，以写入模式
            for time, rooms in self.schedule_2.items():  # 遍历第二个值班表中的每个时间段和对应的值班室列表
                f.write(f"{time}：\n")  # 在文件中写入时间段并换行
                for room, employees in rooms.items():  # 遍历每个值班室和对应的员工列表
                    f.write(f"{room}：")  # 在文件中写入值班室
                    for employee in employees:  # 遍历每个员工
                        f.write(f"{employee.name} ")  # 在文件中写入员工姓名
                    f.write("\n")  # 在文件中换行
                f.write("\n")  # 在文件中换行

        messagebox.showinfo("提示", f"已同意{source_employee.name}与您在{apply[2]}调班，并更新了值班表")  # 弹出提示框显示同意成功信息

    def refuse_apply(self):
        """拒绝调班申请方法，根据选择的申请信息，向申请者发送拒绝信息，并从申请列表中删除该申请信息"""

        index = int(self.apply_text.index(tk.INSERT).split(".")[0]) - 1  # 获取文本框中光标所在行数减一，作为选择的申请信息在申请列表中的索引
        apply = self.applies[index]  # 获取选择的申请信息

        source_employee = apply[0]  # 将要调班的源员工设为申请信息中的源员工对象
        target_employee = apply[1]  # 将要调班的目标员工设为申请信息中的目标员工对象

        messagebox.showinfo("提示", f"已向{source_employee.name}发送拒绝信息")  # 弹出提示框显示拒绝成功信息
        self.applies.remove(apply)  # 从申请列表中移除该申请信息

    def view_schedule(self):
        """查看值班表方法，显示当前登录的员工所属值班室的两个时间段的值班表"""

        self.main_frame.pack_forget()  # 隐藏主菜单界面的框架
        self.view_frame = tk.Frame(self.window)  # 创建查看值班表界面的框架
        self.view_frame.pack()
        tk.Label(self.view_frame, text="您所属值班室的值班表如下：", font=("宋体", 16)).pack(pady=20)
        self.schedule_text = tk.Text(self.view_frame)  # 创建值班表文本框，用于显示值班表信息
        self.schedule_text.pack()
        for time, rooms in self.schedule_1.items():  # 遍历第一个值班表中的每个时间段和对应的值班室列表
            self.schedule_text.insert(tk.END, f"{time}：\n")  # 在文本框中插入时间段并换行
            for room, employees in rooms.items():  # 遍历每个值班室和对应的员工列表
                if room == self.current_user.room:  # 如果该值班室与当前登录的员工所属的值班室相同
                    self.schedule_text.insert(tk.END, f"{room}：")  # 在文本框中插入值班室
                    for employee in employees:  # 遍历每个员工
                        self.schedule_text.insert(tk.END, f"{employee.name} ")  # 在文本框中插入员工姓名
                    self.schedule_text.insert(tk.END, "\n")  # 在文本框中换行
            self.schedule_text.insert(tk.END, "\n")  # 在文本框中换行

        for time, rooms in self.schedule_2.items():  # 遍历第二个值班表中的每个时间段和对应的值班室列表
            self.schedule_text.insert(tk.END, f"{time}：\n")  # 在文本框中插入时间段并换行
            for room, employees in rooms.items():  # 遍历每个值班室和对应的员工列表
                if room == self.current_user.room:  # 如果该值班室与当前登录的员工所属的值班室相同
                    self.schedule_text.insert(tk.END, f"{room}：")  # 在文本框中插入值班室
                    for employee in employees:  # 遍历每个员工
                        self.schedule_text.insert(tk.END, f"{employee.name} ")  # 在文本框中插入员工姓名
                    self.schedule_text.insert(tk.END, "\n")  # 在文本框中换行
            self.schedule_text.insert(tk.END, "\n")  # 在文本框中换行

    def exit_system(self):
        """退出系统方法，关闭窗口并退出程序"""

        answer = messagebox.askyesno("提示", "您确定要退出吗？")  # 弹出确认框询问是否确定退出
        if answer:  # 如果回答是
            self.window.destroy()  # 销毁窗口对象

    def run(self):
        pass


if __name__ == "__main__":  # 如果当前模块是主模块
    system = ScheduleSystem()  # 创建排班管理系统对象
    system.run()  # 调用run方法运行程序
    system.window.mainloop()