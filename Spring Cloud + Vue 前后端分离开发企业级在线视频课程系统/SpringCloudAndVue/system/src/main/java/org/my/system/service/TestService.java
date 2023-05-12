package org.my.system.service;

import org.my.system.domain.Test;
import org.springframework.validation.annotation.Validated;

import java.util.List;


@Validated
public interface TestService {

    List<Test> list();
}
