package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.oauth2.config.annotation.web.configuration.EnableAuthorizationServer;
import org.springframework.security.web.authentication.LoginUrlAuthenticationEntryPoint;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;


@SpringBootApplication
@EnableAuthorizationServer
public class AuthserverApplication extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
	http.antMatcher("/**").authorizeRequests().antMatchers("/")
	    .permitAll().anyRequest().authenticated()
	    .and().exceptionHandling()
	    .authenticationEntryPoint(new LoginUrlAuthenticationEntryPoint("/"));
    }

    public static void main(String[] args) {
	SpringApplication.run(AuthserverApplication.class, args);
    }

}

