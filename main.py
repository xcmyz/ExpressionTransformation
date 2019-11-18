from module import parse_input, write_exp, assign
from module import cal_postfix_expression, compound_inexp, print_expression
from transfer import pre2in, in2post, in2pre
from tree import PostExpTree, front_digui
from visualize import draw


if __name__ == "__main__":
    test_examples = ["+ a * b c", " + * 5 ^ x 2 * 8 x",
                     "+ * 3 ^ * 3 * 2 ^ x 2 x 6"]

    inexp_list = list()
    for ind, test_example in enumerate(test_examples):
        print()
        pre_exp = parse_input(test_example)
        in_exp = pre2in(pre_exp)
        post_exp = in2post(in_exp)
        pre_exp = in2pre(in_exp)

        print("prefix expression:", print_expression(pre_exp))
        print("infix expression:", print_expression(in_exp))
        print("postfix expression:", print_expression(post_exp))
        # print("write expression from infix expression:", write_exp(in_exp))

        if ind == 1 or ind == 2:
            assigned_post = assign("x", 3, post_exp)
            print("assign result:", cal_postfix_expression(assigned_post))
            inexp_list.append(in_exp)

    # Visualize
    root_add_id = PostExpTree(in2post(compound_inexp(
        inexp_list[0], inexp_list[1])), add_id=True)
    draw(root_add_id)
