import enum

import flax.linen
import jax

import mtrl.nn.initializers


class Initializer(enum.Enum):
    ZEROS = enum.member(lambda: jax.nn.initializers.zeros)  # noqa: E731
    HE_NORMAL = enum.member(jax.nn.initializers.he_normal)
    HE_UNIFORM = enum.member(jax.nn.initializers.he_uniform)
    XAVIER_NORMAL = enum.member(jax.nn.initializers.xavier_normal)
    XAVIER_UNIFORM = enum.member(jax.nn.initializers.xavier_uniform)
    CONSTANT = enum.member(jax.nn.initializers.constant)
    UNIFORM = enum.member(mtrl.nn.initializers.uniform)

    def __call__(self, *args):
        return self.value(*args)


class Activation(enum.Enum):
    ReLU = enum.member(jax.nn.relu)
    Tanh = enum.member(jax.nn.tanh)
    LeakyReLU = enum.member(jax.nn.leaky_relu)
    PReLU = enum.member(lambda x: flax.linen.PReLU()(x))  # noqa: E731
    ReLU6 = enum.member(jax.nn.relu6)
    SiLU = enum.member(jax.nn.silu)
    GELU = enum.member(jax.nn.gelu)
    GLU = enum.member(jax.nn.glu)
    # TODO: Add SwiGLU

    def __call__(self, *args):
        return self.value(*args)