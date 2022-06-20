package com.mp.first;

import com.baomidou.mybatisplus.core.conditions.Wrapper;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.toolkit.Wrappers;
import com.mp.first.dao.UserMapper;
import com.mp.first.entity.User;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.sql.Array;
import java.time.LocalDateTime;
import java.util.*;

@SpringBootTest
@RunWith(SpringRunner.class)
class RetrieveTests {

    @Autowired
    private UserMapper userMapper;

    @Test
    public void selectById() {
        User user = userMapper.selectById(1094590409767661570l);
        System.out.println(user);
    }

    @Test
    public void selectIds() {
        List<Long> list = Arrays.asList(1088250446457389058l, 1094590409767661570l, 1094592041087729666l);
        List<User> userList = userMapper.selectBatchIds(list);
        userList.forEach(System.out::println);
    }

    @Test
    public void selectByMap() {
//        map.put("name","王天风")
//        map.put("age",30")
//        where name = "王天风" and age = 30
        Map<String, Object> map = new HashMap<>();
//        map.put("name","王天风");
        map.put("age", 31);
        List<User> userList = userMapper.selectByMap(map);
        userList.forEach(System.out::println);
    }

    /**
     * 1.名字中包含雨，并且年龄小于40
     */
    @Test
    public void selectByWrapper() {
        QueryWrapper<User> userQueryWrapper = new QueryWrapper<>();
//        方法2
//        QueryWrapper<User> query = Wrappers.<User>query();
        userQueryWrapper.like("name", "雨").lt("age", 40);
        List<User> userList = userMapper.selectList(userQueryWrapper);
        userList.forEach(System.out::println);
    }

    /**
     * 2.名字中包含雨，并且年龄大于等于10且小于等于40，并且email不为空
     */
    @Test
    public void selectByWrapper2() {
        QueryWrapper<User> userQueryWrapper = new QueryWrapper<>();
        userQueryWrapper.like("name", "雨").between("age", 20, 40).isNotNull("email");
        List<User> userList = userMapper.selectList(userQueryWrapper);
        userList.forEach(System.out::println);
    }

    /**
     * 3.名字为王姓或者年龄大于等于25，按照年龄降序排列，年龄相同按照id升序排列
     */
    @Test
    public void selectByWrapper3() {
        QueryWrapper<User> userQueryWrapper = new QueryWrapper<>();
        userQueryWrapper.likeRight("name", "王").or().ge("age", 25).orderByDesc("age").orderByAsc("id");
        List<User> userList = userMapper.selectList(userQueryWrapper);
        userList.forEach(System.out::println);
    }

    /**
     * 4.创建日期为2019年2月14日并且直属上级为王姓
     */
    @Test
    public void selectByWrapper4() {
        QueryWrapper<User> userQueryWrapper = new QueryWrapper<>();
        userQueryWrapper.apply("date_format(create_time,'%Y-%m-%d')={0}","2019-02-14")
                .inSql("manager_id","select id from user where name like '王%'");
        List<User> userList = userMapper.selectList(userQueryWrapper);
        userList.forEach(System.out::println);
    }

    /**
     * 5、姓名为王姓，并且（年龄小于40或邮箱不为空）
     */
    @Test
    public void selectByWrapper5() {
        QueryWrapper<User> userQueryWrapper = new QueryWrapper<>();
        userQueryWrapper.likeRight("name","王").and(wq->wq.lt("age","40").or().isNotNull("email"));
        List<User> userList = userMapper.selectList(userQueryWrapper);
        userList.forEach(System.out::println);
    }

    /**
     * 6、姓名为王姓或者（年龄小于40并且年龄大于20并且邮箱不为空）
     */
    @Test
    public void selectByWrapper6() {
        QueryWrapper<User> userQueryWrapper = new QueryWrapper<>();
        userQueryWrapper.likeRight("name","王").or(wq->wq.lt("age",40).gt("age",20).isNotNull(
                "email"));
        List<User> userList = userMapper.selectList(userQueryWrapper);
        userList.forEach(System.out::println);
    }

    /**
     * 7、（年龄小于40或邮箱不为空）并且名字为王姓
     */
    @Test
    public void selectByWrapper7() {
        QueryWrapper<User> userQueryWrapper = new QueryWrapper<>();
        userQueryWrapper.nested(wq->wq.lt("age",40).isNotNull("email")).likeRight("name","王");
        List<User> userList = userMapper.selectList(userQueryWrapper);
        userList.forEach(System.out::println);
    }

    /**
     * 8、年龄为30、31、34、35
     */
    @Test
    public void selectByWrapper8() {
        QueryWrapper<User> userQueryWrapper = new QueryWrapper<>();
        userQueryWrapper.in("age",Arrays.asList(30,31,34,35));
        List<User> userList = userMapper.selectList(userQueryWrapper);
        userList.forEach(System.out::println);
    }

    /**
     * 9、只返回满足条件的其中一条语句即可
     */
    @Test
    public void selectByWrapper9() {
        QueryWrapper<User> userQueryWrapper = new QueryWrapper<>();
        userQueryWrapper.in("age",Arrays.asList(31,30,34,35)).last("limit 1");
        List<User> userList = userMapper.selectList(userQueryWrapper);
        userList.forEach(System.out::println);
    }
}
