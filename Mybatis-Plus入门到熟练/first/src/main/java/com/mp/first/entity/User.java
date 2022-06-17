package com.mp.first.entity;

import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.time.LocalDateTime;

@Data
@TableName("mp_user")
public class User {

    //    主键
    @TableId
    private Long userId;
    //    姓名
    @TableField("name")
    private String realName;
    //    年龄
    private Integer age;
    //    邮箱
    private String email;
    //    直属上级
    private Long managerId;
    //    创建时间
    private LocalDateTime createTime;
//    方法1
    private transient String remark1;
//    方法2
    private static String remark2;

    public static String getRemark2() {
        return remark2;
    }

//    方法3
    @TableField(exist = false)
    public String remark3;

    public static void setRemark2(String remark2) {
        User.remark2 = remark2;
    }
}
