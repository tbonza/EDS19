package com.example.demo;

import java.security.Principal;
import java.util.Collections;
import java.util.Map;

import javax.servlet.http.HttpSession;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.security.SecurityProperties;
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.annotation.Order;
import org.springframework.security.config.annotation.web.
    builders.HttpSecurity;
import org.springframework.security.config.annotation.web.
    configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.web.csrf.CookieCsrfTokenRepository;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@SpringBootApplication
@Controller
@EnableZuulProxy
public class UiApplication {

    public static void main(String[] args) {
	SpringApplication.run(UiApplication.class, args);
    }

    @Configuration
    @Order(SecurityProperties.IGNORED_ORDER)
    protected static class SecurityConfiguration
	extends WebSecurityConfigurerAdapter {

	@Override
	protected void configure(HttpSecurity http) throws Exception {
	    // @formatter:off
	    http
		.httpBasic().and()
		.logout().and()
		.authorizeRequests()
		  .antMatchers("/index.html", "/", "/home", "/login")
		  .permitAll()
		  .anyRequest().authenticated().and()
		.csrf()
		  .csrfTokenRepository(CookieCsrfTokenRepository
				     .withHttpOnlyFalse());
	    // @formatter: on
	}
    }

    @GetMapping("/token")
    @ResponseBody
    public Map<String,String> token(HttpSession session){
	return Collections.singletonMap("token", session.getId());
    }
}

