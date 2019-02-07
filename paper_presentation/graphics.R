# Graphics for Perils Paper presentation

library(ggplot2)


# Table 5 graphic

t5 <- tibble(
`Peril` = c("PI", "PII", "PIII", "PV", "PVII", "PX"),
`PII` = c(22, NA, 24, 12, 19, 14),
`PIII` = c(83, 93, NA, 78, 70, 70),
`PV` = c(20,12,19, NA, 25, 0),
`PVII` = c(66, 70, 71, 59, NA, 52),
`PX` = c(25, 15, 20, 42, 37, NA)
)

tg5 = tibble(
    r_peril = factor(c("PI", "PI", "PI","PI", "PI",
                "PII", "PII", "PII", "PII",
                "PIII", "PIII", "PIII", "PIII",
                "PV", "PV", "PV", "PV",
                "PVII", "PVII", "PVII", "PVII",
                "PX", "PX", "PX", "PX")),
    c_peril = factor(c("PII","PIII","PV","PVII", "PX",
                "PIII","PV","PVII", "PX",
                "PII","PV","PVII", "PX",
                "PII", "PIII", "PVII", "PX",
                "PII","PIII","PV","PX",
                "PII","PIII","PV","PVII")),
    obs     = c(22, 83, 20, 66, 25,
                93, 12, 70, 15,
                24, 19, 71, 20,
                12, 78, 59, 42,
                19, 70, 25, 37,
                14, 70, 0, 52)
)

f1 <- ggplot(tg5, aes(c_peril, r_peril)) +
    geom_tile(aes(fill=obs)) +
    scale_fill_distiller(palette = "Spectral") +
    theme(axis.title.x=element_blank(),
          axis.title.y=element_blank(),
          text=element_text(size=16, face="bold"))
ggsave("imgs/table5_revamp.png", f1)

# Redo Table 2

tg2 <- tibble(
    `Category of use` = factor(c("Software development", "Experimental",
                          "Storage", "Academic", "Web",
                          "No longer accessible", "Empty")),
    `Number of repositories` = c(275,53,36,31,25,11,3),
    percentage = c(63.4, 12.2, 8.3, 7.1, 5.8, 2.5, 0.7)
)

f2 <- ggplot(tg2, aes(`Category of use`, `Number of repositories`)) +
    geom_col(aes(fill=percentage)) + coord_flip() +
    scale_fill_distiller(palette = "Spectral") +
    theme(axis.text.y = element_text(angle=45)) +
    labs(title="(Table 2) Number of repositories per type of use",
         subtitle="Mutually exclusive categories for the manual inspection",
         x="Number of Repositories", y="Category of Use")
ggsave("imgs/table2_revamp.png", f2)


# Table 3 redo

tg3 <- tibble(
    `Set` = c("Located on Sourceforge",
              "Located on Bitbucket", "From subversion repos",
              "From mercurial repos", "From CVS repos"),
    `Projects` = c(117, 91, 622, 113, 55),
    `Repos` = c(511, 249, 4966, 590, 212)
)

f3 <- ggplot(tg3, aes(`Set`, `Repos`, fill=`Projects`)) +
    geom_col() + coord_flip() +
    scale_fill_distiller(palette = "Spectral") +
    theme(axis.text.y = element_text(angle=45)) +
    labs(title="(Table 3) Repositories hosted on GitHub labeled as mirrors")
ggsave("imgs/table3_revamp.png", f3)
