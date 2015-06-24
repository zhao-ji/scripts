standard_deviation = lambda li: (
    sum(
        map(
            lambda i: i*i,
            li,
        )
    )
    /
    float(
        len(li)
    )
    -
    (
        sum(li)
        /
        float(
            len(li)
        )
    ) ** 2
) ** (
    1
    /
    float(2)
)
