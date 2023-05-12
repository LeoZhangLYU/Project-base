package org.my.system.service.impl;

import jakarta.annotation.Resource;
import org.my.system.domain.Test;
import org.my.system.mapper.TestMapper;
import org.my.system.service.TestService;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TestServiceImpl implements TestService {

    @Resource
    private TestMapper testMapper;

    @Override
    public List<Test> list() {
        return testMapper.list();
    }
}
